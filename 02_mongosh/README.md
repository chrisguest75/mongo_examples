# README

Demonstrate management commands through `mongosh`  

Startup a new mongodb with a userdb and also demonstrate importing.  

Ref: 23_faking_json_data [here](https://github.com/chrisguest75/typescript_examples/tree/master/23_faking_json_data)  

TODO:  

* query and export data.  

## Startup

```sh
# list profiles
docker compose config --profiles

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker compose logs mongodb          
```

## Rebuild backend and run

```sh
# if changes are made to backend rerun
docker compose --profile backend up -d --build
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

```sh
# import the data
mongoimport -c files --file ./data/file.json "mongodb://root:rootpassword@0.0.0.0:27017/db1" --authenticationDatabase admin -vvv 

#--fields="size.int32(),id.string(),file.string(),deleted.boolean(),email.string(),name.string(),created.date(2021-11-05T06:32:52.474Z),updateed.date(2021-11-05T06:32:52.474Z)"
```

## Query the data in mongosh

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/admin"

# switch into db
use db1 

# find documents
db.files.find()

db.files.explain().find()

# show type for created field
db.files.aggregate( 
    [ 
        { "$project": { "fieldType": {  "$type": "$created"  } } } 
    ]
)

# drop collection
db.files.drop()
```

## Query the data using scripts

```sh
# list the deleted files
mongosh --quiet "mongodb://root:rootpassword@0.0.0.0:27017" ./scripts/find_deleted_files.js | jq .

# daterange (not working because of the date field type)
mongosh --quiet "mongodb://root:rootpassword@0.0.0.0:27017" ./scripts/find_daterange_files.js | jq .
```

## Cleanup

```sh
# bring it down and delete the volume
docker compose --profile backend down --volumes
```

## Resources

* Database Commands [here](https://docs.mongodb.com/manual/reference/command/)  
* mongodb-extended-json [here](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/)  
* bson npm package [here](https://www.npmjs.com/package/bson)  