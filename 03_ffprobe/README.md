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

```sh
# load all documents
./ffprober/import_probe_data.sh --path=./ffprober/out      
```


Example queries https://github.com/chrisguest75/docker_build_examples/tree/master/45_docker_scan_process_mongo

```js
Questions:
* distinct resolutions
* counts of most common number of streams (video and audio)
* most common video and audio codecs
* framerates 
* sample_rates 
* audio channels
* captions



// count all items in collection
db.getCollection('ffprobe').count()

// count streams for each document
db.getCollection('ffprobe').aggregate([{$project: { count: { $size:"$streams" }}}])

// find items with only one stream
db.getCollection('ffprobe').find({streams: { $size: 1 }});


db.getCollection('ffprobe').distinct("streams.codec_type")
db.getCollection('ffprobe').distinct("streams.width")
db.getCollection('ffprobe').distinct("streams.height")

// distinct resolutions
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'video'} },
    
    { $project: { _id: 0, file: 1, width: { $toString:"$streams.width" }, height: { $toString:"$streams.height" } } },     
    { $project: { file: 1, resolution: { $concat: [ "$width", "x","$height" ] } } }   
])

// distinct codec_long_name
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'video'} },
    
    { $project: { file: 1, width: { $toString:"$streams.width" }, height: { $toString:"$streams.height" } } },     
    { $project: { file: 1, resolution: { $concat: [ "$width", "x","$height" ] } } },   
  {$group: {_id: null, resolutions: {$addToSet: "$resolution"}}}
])

// most common video and audio codecs
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'video'} },
  {$group: {_id: null, uniqueValues: {$addToSet: "$streams.codec_long_name"}}}
])

// most common audio codecs
db.getCollection('ffprobe').aggregate([
  { $unwind: '$streams' },
  { $match: {'streams.codec_type': 'audio'} },
  {$group: {_id: null, uniqueValues: {$addToSet: "$streams.codec_long_name"}}}
])

// group files into audio codec type
db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
   { $group : { _id : "$streams.codec_long_name", books: { $push: "$file" } } }
 ])

// count of the audio codec types
 db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
   { $group : { _id : "$streams.codec_long_name", count: { $count: {} } } }
 ])

// count of the video codec types
 db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'video'} },
   { $group : { _id : "$streams.codec_long_name", count: { $count: {} } } }
 ])  

  db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
   { $group : { _id : "$streams.sample_rate", count: { $count: {} } } }
 ])  

//audio sample rates
   db.getCollection('ffprobe').aggregate([
    { $unwind: '$streams' },
    { $match: {'streams.codec_type': 'audio'} },
   { $group : { _id : "$streams.sample_rate", count: { $count: {} } } }
 ])  
```







```sh
mongosh "mongodb://0.0.0.0:27017/test?retryWrites=true&w=majority" 

mongosh "mongodb://user:userpassword@/0.0.0.0:27017/ffprobe?retryWrites=true&w=majority"
```

## Cleanup

```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

## Resources
https://newbedev.com/concatenate-string-values-in-array-in-a-single-field-in-mongodb