
console.log("Starting...")
db = db.getSiblingDB('newdb')

console.log("Dropping collection1")
db.collection1.drop()

console.log("Dropping user newdb")
try {
    db.runCommand({
        dropUser: "newdb"
    })    
} catch (error) {
    console.error(error);
}

console.log("Creating user newdb")
db.createUser({
    user: "newdb",
    pwd: "newdbpassword",
    roles: [ { role: "readWrite", db: "newdb" } ]
})

console.log("Creating index")
db.collection1.createIndex({ id: 1 }, { unique: true })

console.log("Insert value")
db.collection1.insert({ id: 1, value: 'hello' })
const items = db.collection1.find()
console.log(items)
