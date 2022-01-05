# README

Walkthrough some examples of how to troubleshoot mongodb databases and collections.  

TODO:

* logs
* journal

## Connect to DB

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"
docker exec -it $(docker ps --filter name=03_ffprobe-mongodb-1 -q) /bin/bash

# logs
docker logs $(docker ps --filter name=03_ffprobe-mongodb-1 -q) 

```

## Get versions

```js
# 
db.version()
db.serverBuildInfo()
```

## DB statistics

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

db.[collection name].stats()
db.printCollectionStats()
```

## Profiling

```js

db.getProfilingStatus()


db.setProfilingLevel(2,{slowms: 200})

// And we find out operation
db.system.profile.find({millis: {$gt: 1000}}).pretty()
```

## Document Sizes


```js
Object.bsonsize(db.getCollection('prod').findOne({_id:"111111111"}))

db.getCollection('prod').aggregate([
  {
    "$project": {
      "_id_": 1,
      "object_size": { "$bsonSize": "$$ROOT" }
    }
  }
])

```

ObjectID
http://docs.mongodb.org/manual/reference/object-id/

explain

db.schedules.validate()

Db.oplog.find().pretty()


db.MyLogs.ensureIndex({'timecode' : 1})





## Resources  

* How to Use the MongoDB Profiler and explain() to Find Slow Queries [here](https://studio3t.com/knowledge-base/articles/mongodb-query-performance/)

https://docs.mongodb.com/manual/reference/operator/aggregation/bsonSize/

http://docs.mongodb.org/meta-driver/latest/legacy/mongodb-wire-protocol/

