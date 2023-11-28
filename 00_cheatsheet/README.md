# README

A cheatsheet for Mongo.

* Querying Examples [here](../04_querying_examples/README.md)  

TODO:

* Why is mongo export broken on ubuntu tap install?

## VSCode

```sh
code --install-extension mongodb.mongodb-vscode
```

## Tools

NOTE: This also work on linuxbrew for `mongosh`. 

```sh
brew tap mongodb/brew

# new mongosh
brew info mongosh

# mongeexport, etc
brew info mongodb-database-tools
ls -la $(brew --prefix mongodb-database-tools)
```

## Resources

* mongodb-js/mongosh [repo](https://github.com/mongodb-js/mongosh#readme)  
* Installing the Database Tools on macOS [here](https://www.mongodb.com/docs/database-tools/installation/installation-macos/#installation)  
