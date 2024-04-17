# MongoDB Examples and Demos

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)  

A repository for showing examples of working with Mongo  

## Conventional Commits

NOTE: This repo has switched to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0). It requires `pre-commit` and `commitizen` to help with controlling this.  

```sh
# install pre-commmit (prerequisite for commitizen)
brew install pre-commit
brew install commitizen
# conventional commits extension
code --install-extension vivaxy.vscode-conventional-commits

# install hooks
pre-commit install --install-hooks --overwrite --config .pre-commit-config.yaml
```

Python example REF:[chrisguest75/python_examples/14_mongo](https://github.com/chrisguest75/python_examples/tree/main/14_mongo)  

## 00 - Cheatsheet

A cheatsheet for Mongo.  
Steps [README.md](./00_cheatsheet/README.md)  

## 01 - MERN

Demonstrate an example of using MERN stack  
Steps [README.md](./01_mern/README.md)  

## 02 - Mongosh

Demonstrate management commands through `mongosh`  
Steps [README.md](./02_mongosh/README.md)  

## 03 - ffprobe

Create a small application that can be used to query ffprobe data  
Steps [README.md](./03_ffprobe/README.md)  

## 04 - Querying Examples

Show some querying examples.  
Steps [README.md](./04_querying_examples/README.md)  

## 06 - Visualising with dash

Demonstrate how to connect `dash` to `mongo`  
Steps [README.md](./06_dash/README.md)  

## 07 - Troubleshooting

Walkthrough some examples of how to troubleshoot `mongodb` databases and collections.  
Steps [README.md](./07_troubleshooting/README.md)  

## 09 - Exporting

Demonstrate exporting data from mongo.  
Steps [README.md](./09_exporting/README.md)  

## Resources

* Some other querying examples in docker_examples [here](https://github.com/chrisguest75/docker_examples/tree/master/45_docker_scan_process_mongo)
