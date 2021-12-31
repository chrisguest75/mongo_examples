# README

TODO:
* logs
* journal

```js
db.stats()
db.MyLogs.stats()
db.printCollectionStats()
system.indexes
```

https://docs.mongodb.com/manual/reference/operator/aggregation/bsonSize/

http://docs.mongodb.org/meta-driver/latest/legacy/mongodb-wire-protocol/

ObjectID
http://docs.mongodb.org/manual/reference/object-id/

explain

db.schedules.validate()

Db.oplog.find().pretty()

	• db.version()
Db.serverBuildInfo()

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
