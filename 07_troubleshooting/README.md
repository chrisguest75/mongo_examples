# README

Walkthrough some examples of how to troubleshoot mongodb databases and collections.  

TODO:

* logs
* journal

## Connect to DB

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"
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



system.indexes
```


ObjectID
http://docs.mongodb.org/manual/reference/object-id/

explain

db.schedules.validate()

Db.oplog.find().pretty()


db.MyLogs.ensureIndex({'timecode' : 1})


db.setProfilingLevel(2,{slowms: 200})
db.students.aggregate([
    {$sort: {"age": -1}},
    {$match: {"age": {$lt: 15}}},
    {$group: {_id: "$grade",frequency: {$sum: 1}}},
    {$match: {"frequency": {$gt: 10}}}
 ])

// And we find out operation
db.system.profile.find({millis: {$gt: 1000}}).pretty()



## Resources 

https://docs.mongodb.com/manual/reference/operator/aggregation/bsonSize/

http://docs.mongodb.org/meta-driver/latest/legacy/mongodb-wire-protocol/
