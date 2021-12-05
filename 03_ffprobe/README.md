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

db.getCollection('ffprobe').find({})
db.getCollection('ffprobe').createIndex(
  {
      "md5": 1
  },
  {
      unique: true
  }
)

# load all documents
./ffprober/import_probe_data.sh --path=./ffprober/out      
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
