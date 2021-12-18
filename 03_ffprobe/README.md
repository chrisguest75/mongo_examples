# README

Create a small application that can be used to query ffprobe data

TODO:

* Load db.
* Extract a set of ffprobe data from my shares
* Load it into db
* Write some queries to classify it.  

## Startup

```sh
# list profiles
docker compose config --profiles               

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker logs $(docker ps --filter name=03_ffprobe-mongodb-1 -q)
```

## Rebuild backend and run

```sh
# if changes are made to backend rerun
docker-compose --profile backend up -d --build
```

## Connect to mongosh

```sh
mongoimport -c ffprobe --file ./ffprober/out/03e548bb050685008105484690c578d2.json "mongodb://root:rootpassword@0.0.0.0:27017/ffprobe" --authenticationDatabase admin

mongosh "mongodb://user:userpassword@/0.0.0.0:27017/"

mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"

> use ffprobe
```

```js
// check mongodb version
db.version()

db.getCollection('ffprobe').find({})
db.getCollection('ffprobe').createIndex(
  {
      "md5": 1
  },
  {
      unique: true
  }
)
```

## FFProber

Included is a tool called `ffprober` that I've written to go through directories of media files and dump the ffprobe data out.  It also adds some useful extra fields such as an MD5, filesize, filename and GOP structure.  

ffprober [readme.md](/ffprober/README.md)  

```sh
# load all ffprober documents
./ffprober/import_probe_data.sh --path=./ffprober/out      
```

## Querying

When writing queries I find it useful to state the questions first.  

Questions:

* What are the distinct resolutions?
* What are the counts of most common number of streams (video and audio)?
* What are the most common video and audio codecs?
* What are the framerates?
* What are the sample_rates?
* Are there any captions?

```js
// count all items in collection
db.getCollection('ffprobe').count()

// count streams for each document
db.getCollection('ffprobe').aggregate([
  {$project: { count: { $size:"$streams" }}
}])

// find items with only one stream
db.getCollection('ffprobe').find({streams: { $size: 1 }});


db.getCollection('ffprobe').distinct("streams.codec_type")
db.getCollection('ffprobe').distinct("streams.codec_name")
db.getCollection('ffprobe').distinct("streams.width")
db.getCollection('ffprobe').distinct("streams.height")

// all codecs
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $project: { file: 1, codec: { $concat: [ "$streams.codec_type", " ","$streams.codec_name" ] } } },   
  {$group: {_id: null, codecs: {$addToSet: "$codec"}}}
])

// codecs grouped by type
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  {$group: {_id: "$streams.codec_type", codecs: {$addToSet: "$streams.codec_name" }}}
])

// sample rates and bit rates
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
{ $project: { _id: 0, file: 1, codec_long_name:{ $toString:"$streams.codec_long_name" }, sample_rate: { $toString:"$streams.sample_rate" }, bit_rate: { $toString:"$streams.bit_rate" } } }, 

  { $project: { file: 1, codec_long_name:1, audiorate: { $concat: [ "$sample_rate", "khz - ", "$bit_rate", "bps"] } } },   
  {$group: {_id: "$codec_long_name", audiorates: {$addToSet: "$audiorate"}}}
])

// resolution of each file
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'video'} },
    
    { $project: { _id: 0, file: 1, width: { $toString:"$streams.width" }, height: { $toString:"$streams.height" } } },     
    { $project: { file: 1, resolution: { $concat: [ "$width", "x","$height" ] } } }   
])

// distinct resolution
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'video'} },
    
    { $project: { file: 1, width: { $toString:"$streams.width" }, height: { $toString:"$streams.height" } } },     
    { $project: { file: 1, resolution: { $concat: [ "$width", "x","$height" ] } } },   
  {$group: {_id: null, resolutions: {$addToSet: "$resolution"}}}
])

// most common audio and video codecs
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  {$group: {_id: "$streams.codec_type", uniqueValues: {$addToSet: "$streams.codec_long_name"}}}
])

// group files into audio and video codec type
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $group : { _id : "$streams.codec_long_name", files: { $push: {file: "$file", codec_long_name: "$streams.codec_type"} } }}
 ])

// count by codec types
db.getCollection('ffprobe').aggregate([
  { $unwind: 'streams' },
  { $group : { _id : "$streams.codec_long_name", count: { $count: {} } } },
  { $sort : { count : -1 } }
])

// count audio only codec
db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
    { $group : { _id : "$streams.codec_long_name", count: { $count: {} } } },
    { $sort : { count : -1 } }
])

//audio sample rates
  db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
   { $group : { _id : "$streams.sample_rate", count: { $count: {} } } }
 ])  

// sorted sample rates
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'audio'} },
  { $group : { _id : "$streams.sample_rate", count: { $count: {} } } },
  { $project: { _id:  { $toInt:"$_id" }, count: 1}},
  { $sort : { _id : 1 } }
])  

// grouped durations
db.getCollection('ffprobe').aggregate([
     { $unwind: '$streams' },
    { "$group": {
        "_id": {
            "$cond": [
                { "$lt": [ { $toDouble:"$streams.duration" } , 10 ] },
                "0-10secs",
                    {"$cond": [
                { "$lt": [ {$toDouble:"$streams.duration"}, 60 ] },
                "10-60secs",
                {"$cond": [
                { "$lt": [ {$toDouble:"$streams.duration"}, 600 ] },
                "60-600secs",
                "600+secs"
            ]}
            ]}

          ]
        },
        "count": { "$sum": 1 },
        "files": { $push: {file: "$file", duration: "$streams.duration"} }
    }}
])    


```

## Cleanup

```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

## Resources

* Concatenate string values in array in a single field in MongoDB [here](https://newbedev.com/concatenate-string-values-in-array-in-a-single-field-in-mongodb)