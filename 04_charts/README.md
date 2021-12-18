# README

## Startup

```sh
# list profiles
docker compose config --profiles               

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker logs $(docker ps --filter name=04_charts-mongodb-1 -q)

# has charts connected?
docker logs $(docker ps --filter name=04_charts-charts-1 -q)

docker compose --profile backend down
```

## Connect to mongosh

```sh
mongoimport -c ffprobe --file ./ffprober/out/03e548bb050685008105484690c578d2.json "mongodb://root:rootpassword@0.0.0.0:27017/ffprobe" --authenticationDatabase admin

mongosh "mongodb://user:userpassword@/0.0.0.0:27017/"

mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"

> use ffprobe
```


## 

```sh
docker run --rm quay.io/mongodb/charts:19.12.2 charts-cli test-connection 'mongodb://root:rootpassword@host.docker.internal'
```


## Cleanup

```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

## Resources

https://gist.github.com/Tallic/9486fb03a1425398be3091f320d23a06

