# README

Demonstrate management commands through `mongosh`  

Startup a new mongodb with a userdb.  

TODO:  

* add data to collections  
* query and export data.  
* processing mongosh scripts from shell

## Startup

```sh
# list profiles
docker compose config --profiles               

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker logs $(docker ps --filter name=02_mongosh-mongodb-1 -q)
```

## Rebuild backend and run

```sh
# if changes are made to backend rerun
docker-compose --profile backend up -d --build
```

## Connect to mongosh as admin

```sh
# connect admin
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/admin"
```

```js
db.version()

// show list of dbs
show dbs
// show 
show users
show roles

// switch db
use startup
// show 
show users
```

## Connect to mongosh as user

```sh
# connect as user
mongosh "mongodb://startup:startuppassword@0.0.0.0:27017/startup"
```

```js
show users

// switch to admin db and see restricted permissions
use admin
show users
```

## Create a new db

```js
mongosh "mongodb://root:rootpassword@0.0.0.0:27017" ./scripts/initialise_db.js
mongosh "mongodb://newdb:newdbpassword@0.0.0.0:27017/newdb"    
show collections
```

## Load db

```js

```

## Cleanup

```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

## Resources

* Database Commands [here](https://docs.mongodb.com/manual/reference/command/)
