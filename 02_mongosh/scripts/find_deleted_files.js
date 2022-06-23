
function getDeletedFiles() {
    const filesdb = db.getSiblingDB('db1')
    const files = filesdb.getCollection('files').find({
        deleted: { $eq: true },
    }, { "_id":1, deleted:1, created:1, file:1}).toArray();
    return files    
    //const ids = files.map((value) => { return { _id: value._id, file: value.file } } ).join("\n");
    //return ids;
}

//console.log("Starting...")
var files = getDeletedFiles()
console.log(JSON.stringify(files));


