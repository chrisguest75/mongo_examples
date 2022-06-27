# README

Walkthrough some examples of how to troubleshoot `mongodb` databases and collections.  

TODO:

* logs
* journal
  * db.oplog.find().pretty()
* Symptoms
  * Very slow queries
  * Response time degradation
  * Application pauses
  * High disk IO
  * Incorrect filesystem configuration
  * Incorrect MongoDB configuration
    * Write concerns
  * Application driver misconfiguration
  * Connectivity issues
  * Cluster configuration issues
  * Replica sets on sharded clusters
* database profiler, compass - 
* mtools - martiin rueckstiess - tools to parse and visualise the log files.  

## Setup

* 02_mongosh [here](../02_mongosh/README.md)
* 07_ffprobe [here](../07_ffprobe/README.md)

## List of tools

### mongostat

Monitor basic MongoDB server statistics.

```sh
mongostat --username=root --password=rootpassword --host "0.0.0.0" --port "27017" --authenticationDatabase=admin
```

```txt
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
    *0    *0     *0     *0       0     1|0  0.0% 0.1%       0 1.51G 113M 0|0 0|0   113b   57.0k    9 Jun 24 23:15:51.553
    *0     2      1     *0       0     3|0  0.0% 0.1%       1 1.51G 113M 0|0 0|0   112b   56.1k    9 Jun 24 23:15:52.552
    *0    *0     *0     *0       0     1|0  0.0% 0.1%       0 1.51G 113M 0|0 0|0   112b   56.2k    9 Jun 24 23:15:53.549 
```

### mongotop

Monitor basic usage statistics for each collection.

```sh
mongotop --username=root --password=rootpassword --host "0.0.0.0" --port "27017" --authenticationDatabase=admin
```

```txt
                    ns    total    read    write    2022-06-24T23:18:04+01:00
    admin.system.users      0ms     0ms      0ms                             
  admin.system.version      0ms     0ms      0ms                             
config.system.sessions      0ms     0ms      0ms                             
   config.transactions      0ms     0ms      0ms                             
             db1.files      0ms     0ms      0ms                             
             db1.oplog      0ms     0ms      0ms                             
    db1.system.profile      0ms     0ms      0ms                             
  local.system.replset      0ms     0ms      0ms     
```

## Connect to DB using mongosh

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"

# logs
docker compose logs mongodb

# enter the container
docker compose exec -it mongodb /bin/bash

cat /etc/mongod.conf.orig 
ls /data/db/journal/
```

### Logs

Server logs:

* Queries are taking a long time to answer - first place to look. This is the first thing support asks for.  
* Time, Sev, Component, Context, Message
  * ACCESS, COMMND, CONTROL, GEO, INDEX, QUERY, REPL, SHARDING, STORAGE, JOURNAL, WRITE

### Get versions

```js
// returns the server version
db.version()
// server build info
db.serverBuildInfo()
```

### DB statistics

```js
use <db>
db.stats()

{
  db: 'ffprobe',
  collections: 2,
  views: 0,
  objects: 9587556,
  avgObjSize: 1256.306391743631,
  dataSize: 12044907884,
  storageSize: 2523344896,
  freeStorageSize: 1413120,
  indexes: 3,
  indexSize: 300945408,
  indexFreeStorageSize: 356352,
  totalSize: 2824290304,
  totalFreeStorageSize: 1769472,
  scaleFactor: 1,
  fsUsedSize: 61297049600,
  fsTotalSize: 62725623808,
  ok: 1
}

// collection stats
db.[collection name].stats()
db.printCollectionStats()
```

### Profiling

```js
// get the current profiling status
db.getProfilingStatus()

db.setProfilingLevel(2,{slowms: 200})

// And we find out operation
db.system.profile.find({millis: {$gt: 1000}}).pretty()
```

### Document Sizes

```js
use db1

// NOTE: This doesn't seem to work in mongosh
db.getCollection('files').find()
Object.bsonSize(db.getCollection('files').findOne({_id:"62ba06184668a159085123ef"}))

// aggregation framework bsonsize
db.getCollection('files').aggregate([
  {
    "$project": {
      "_id_": 1,
      "object_size": { "$bsonSize": "$$ROOT" }
    }
  }
])
```

### Field Types

```sh
# show type for created field
db.files.aggregate( 
    [ 
        { "$project": { "fieldType": {  "$type": "$created"  } } } 
    ]
)
```

### Explain

```sh
# explain a collection
db.files.explain().find()
```

```txt
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'db1.files',
    indexFilterSet: false,
    parsedQuery: {},
    queryHash: '8B3D4AB8',
    planCacheKey: 'D542626C',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: { stage: 'COLLSCAN', direction: 'forward' },
    rejectedPlans: []
  },
  command: { find: 'files', filter: {}, '$db': 'db1' },
  serverInfo: {
    host: '321d03f3fd1d',
    port: 27017,
    version: '5.0.9',
    gitVersion: '6f7dae919422dcd7f4892c10ff20cdc721ad00e6'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600
  },
  ok: 1
}
```

### Indexing

Using indices and explain.  

```sh
db.files.explain().find({
  created: {
    $gte: ISODate("2022-03-01T00:00:00.000Z"),
    $lt: ISODate("2022-03-10T00:00:00.000Z")
  }}, {file:1})

# create index
db.db1.createIndex({'created' : 1, 'file' : 1})
db.db1.getIndexes()

# NOTE: This doesn't seem to use the index
db.files.explain().find({
  created: {
    $gte: ISODate("2022-03-01T00:00:00.000Z"),
    $lt: ISODate("2022-03-10T00:00:00.000Z")
  }}, {file:1})

db.db1.dropIndex('created_1')
db.db1.dropIndex('created_1_file_1')
```

### Validate

```sh
# validate a collection
db.files.validate()

{
  ns: 'db1.files',
  nInvalidDocuments: 0,
  nrecords: 1000,
  nIndexes: 1,
  keysPerIndex: { _id_: 1000 },
  indexDetails: { _id_: { valid: true } },
  valid: true,
  repaired: false,
  warnings: [],
  errors: [],
  extraIndexEntries: [],
  missingIndexEntries: [],
  corruptRecords: [],
  ok: 1
}
```

## Resources  

* How to Use the MongoDB Profiler and explain() to Find Slow Queries [here](https://studio3t.com/knowledge-base/articles/mongodb-query-performance/)
* $bsonSize (aggregation) [here](https://docs.mongodb.com/manual/reference/operator/aggregation/bsonSize/)
* How to Calculate MongoDB Document Size in Node.js [here](https://betterprogramming.pub/how-to-calculate-mongodb-document-size-in-node-js-f463b8457f27)
* mongosh-snippets [here](https://github.com/mongodb-labs/mongosh-snippets)
* ObjectID [here](http://docs.mongodb.org/manual/reference/object-id/)
http://docs.mongodb.org/meta-driver/latest/legacy/mongodb-wire-protocol/
