function getDateRangeFiles() {
    const filesdb = db.getSiblingDB('db1')
    const files = filesdb.getCollection('files').find({
        created: {
            $gte: ISODate("2022-03-01T00:00:00.000Z"),
            $lt: ISODate("2022-03-10T00:00:00.000Z")
        }
    }, { "_id":1, created:1, file:1}).toArray();
    return files    
}

//console.log("Starting...")
var files = getDateRangeFiles()
console.log(JSON.stringify(files));

