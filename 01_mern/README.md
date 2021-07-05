# README
Demonstrate an example of using MERN stack

TODO:
* Create the user and db - create a basic init container example in docker compose.


```sh
# start mongo (profiles not working at the mo')
docker compose --profile backend up -d 
```

## Usage
Open a `1st terminal`
```sh
# start mongo
docker compose up -d 
```

```sh
docker exec -it $(docker ps --filter name=01_mern_mongodb_1 -q) /bin/bash
mongo -u root -p rootpassword
```

```js
use myFirstDatabase
db.createUser(
  {
    user: "user",
    pwd: "userpassword",
    roles: [ { role: "readWrite", db: "myFirstDatabase" } ]
  }
)
```

Open a `2nd terminal`
```sh
# start server
cd ./server
./node_modules/.bin/nodemon server.js
```

Open a `3rd terminal`
```sh
# start client
cd ./client
export PORT=3001
npm start
```

Cleanup the services
```sh
# clean up
docker compose down
# remove the created volume
docker volume rm 01_mern_01_mern_data_container
```


# Resources 
* mern-stack [here](https://www.mongodb.com/mern-stack)  
* mern-stack-tutorial [here](https://blog.logrocket.com/mern-stack-tutorial/)  
* official mern-stack-tutorial [here](https://www.mongodb.com/languages/mern-stack-tutorial) 
* connection strings [here[(https://docs.mongodb.com/manual/reference/connection-string/)  