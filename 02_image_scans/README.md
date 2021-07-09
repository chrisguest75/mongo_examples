# README
Demonstrate an example of using mongodb to store image scans 

## Docker Compose App
```sh
# list profiles
docker compose config --profiles               

# start mongo 
docker compose --profile backend up -d 


# quick test
docker logs $(docker ps --filter name=02_image_scans_mongodb_1 -q)

```

### Cleanup
```sh
# bring it down and delete the volume
docker compose --profile backend down --volumes
```

### Rebuild backend and run
```sh
# if changes are made to backend rerun
docker compose --profile backend up -d --build
```



# Resources 

