# ATLAS

Demonstrate using Atlas CLI to create a cluster.  

## Install

```sh
brew install mongodb-atlas-cli
```

## Configure

```sh
atlas auth login

atlas clusters list

# free tier
atlas cluster create testCluster --projectId 621df6b5628b6c17c10528fd --provider AWS --region US_EAST_1 --tier M0 --tag env=dev

# load the sample dataset in the atlas UI or cli
atlas clusters sampleData load testCluster --output json
```

## Connect

```sh
# set environment variables.  
set -a
. ./.env
set +a

# connect 
atlas accessList create --currentIp
mongosh ${MONGODB_URI}
```

## Query

```sh
db.version()

// show list of dbs
show dbs
// show 
show users
show roles
```

## Resources

* Getting Started with MongoDB Atlas Local Search Experience Using Docker [here](https://www.mongodb.com/developer/products/atlas/getting-started-mongodb-atlas-local-search-experience-using-docker/)
* What is the Atlas CLI? [here](https://www.mongodb.com/docs/atlas/cli/current/)
