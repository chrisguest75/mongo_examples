# MongoDB Examples and Demos

A repository for showing examples of working with Mongo

TODO:

* performance monitoring
* multi node mongo cluster
* terraform mongo
Read Preference Modes
5 modes
 - primary only - default
 - primaryPreferred (always read from primary, unless during elections)
 - secondary 
 - secondaryPreferred

 - Nearest
* transaction example
* analysis size of documents
* Live querying against mongo ORM?
* Data sampling for tests
* go through the slides
https://github.com/rueckstiess/mtools
Slave delay

## Example 1 - MERN

Demonstrate an example of using MERN stack  
Steps [README.md](./01_mern/README.md)  

## Example 2 - Mongosh

Demonstrate management commands through `mongosh`  
Steps [README.md](./02_mongosh/README.md)  

## Example 3 - ffprobe

Create a small application that can be used to query ffprobe data  
Steps [README.md](./03_ffprobe/README.md)  

## Example 6 - Visualising with dash

Demonstrate how to connect `dash` to `mongo`  
Steps [README.md](./06_dash/README.md)  

## Resources

* Some other querying examples in docker_build_examples [here](https://github.com/chrisguest75/docker_build_examples/tree/master/45_docker_scan_process_mongo)
