# README
Demonstrate an example of using MERN stack

TODO:
* Create the user and db - create a basic init container example in docker compose.
* React image is not working 
* Make the ping endppoint check connectivity

## Docker Compose App
```sh
# start mongo (profiles not working at the mo')
docker compose --profile backend up -d 

# use the old command for profiles support.  
docker-compose --profile backend up -d 

# quick test
curl http://0.0.0.0:3000/ping 
docker logs $(docker ps --filter name=01_mern_mongodb_1 -q)
docker logs $(docker ps --filter name=01_mern_backend_1 -q) 
```

### Cleanup
```sh
# bring it down and delete the volume
docker-compose --profile backend down --volumes
```

### Rebuild backend and run
```sh
# if changes are made to backend rerun
docker-compose --profile backend up -d --build
```

## Creating
Open a `1st terminal`
```sh
# start mongo
docker compose up -d 

curl http://0.0.0.0:3000/ping 
docker logs $(docker ps --filter name=01_mern_mongodb_1 -q)
docker logs $(docker ps --filter name=01_mern_backend_1 -q) 
```

```sh
docker exec -it $(docker ps --filter name=01_mern_mongodb_1 -q) /bin/bash
mongo -u root -p rootpassword
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

--volumes
https://docs.docker.com/engine/reference/commandline/compose_down/

--scale
https://docs.docker.com/engine/reference/commandline/compose_up/

