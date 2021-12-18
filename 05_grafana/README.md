# README

Grafana requires Enterprise to add mongodb integration

TODO:

* Take some results from mongo and try to graph them in elasticsearch
* 

## Startup

```sh
# list profiles
docker compose config --profiles               

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker logs $(docker ps --filter name=05_grafana-mongodb-1 -q)

# has charts connected?
docker logs $(docker ps --filter name=05_grafana-grafana-1 -q)

docker logs $(docker ps --filter name=05_grafana-elasticsearch-1 -q)

docker logs $(docker ps --filter name=05_grafana-kibana-1 -q)

docker compose --profile backend down
```

Elasticsearch - http://0.0.0.0:9200/
Kibana - http://0.0.0.0:5601/
Grafana - http://0.0.0.0:3000/

## Connect to mongosh

```sh
mongoimport -c ffprobe --file ./ffprober/out/03e548bb050685008105484690c578d2.json "mongodb://root:rootpassword@0.0.0.0:27017/ffprobe" --authenticationDatabase admin

mongosh "mongodb://user:userpassword@/0.0.0.0:27017/"

mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"

> use ffprobe
```




## Cleanup

```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

## Resources

https://gist.github.com/Tallic/9486fb03a1425398be3091f320d23a06

https://levelup.gitconnected.com/docker-compose-made-easy-with-elasticsearch-and-kibana-4cb4110a80d

https://techoverflow.net/2019/04/06/how-to-insert-test-data-into-elasticsearch-6-x/

