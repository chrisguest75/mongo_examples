# README

Demonstrate building a mongodb devcontainer.  

Ref: [github.com/chrisguest75/devcontainer_examples/16_node_mongo](https://github.com/chrisguest75/devcontainer_examples/tree/main/16_node_mongo)  

## Start (vscode)

Use the Remote Containers extension and select "Reopen in Container" or...  

```sh
# inside devcontainer terminal
mongosh mongodb://root:password@0.0.0.0:27017/admin
```

## Troubleshooting

If you have trouble connecting try cleaning out the docker images and volumes and rebuilding without cache.  

## Resources

