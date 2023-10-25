# EXPORTING

Demonstrate exporting data from mongo.  

TODO:

* Show a mongosh aggregation framework script 02_mongosh/README.md

## Tools

```sh
brew tap mongodb/brew

brew info mongodb-database-tools

brew info mongosh
```

## Exporting

It's best to use Read-Only credentials and a secondary when exporting data from mongo.

NOTES:

* You cannot perform aggregation framework queries with mongoexport.  

```sh
# try with limit to test connection
mongoexport -u "myuser" -p "mypassword" mongodb+srv://myserver/mydb --collection mycollection --readPreference=secondary --type=csv --fields "_id,field1,field2,field3,field4,field5" --query '{"_id":{"$ne":0}}' --out ./exports/mycollection.csv --limit 1
```

## Resources

* mongodb-js/mongosh [repo](https://github.com/mongodb-js/mongosh#readme)  
* Installing the Database Tools on macOS [here](https://www.mongodb.com/docs/database-tools/installation/installation-macos/#installation)  
* Connection Strings [here](https://www.mongodb.com/docs/manual/reference/connection-string)  
* Support aggregation framework queries in mongoexport [here](https://jira.mongodb.org/browse/TOOLS-802)  
