
db = db.getSiblingDB('newdb')
db.collection1.drop()
db.runCommand({
    dropUser: "newdb"
})
db.createUser({
    user: "newdb",
    pwd: "newdbpassword",
    roles: [ { role: "readWrite", db: "newdb" } ]
})
db.collection1.createIndex({ id: 1 }, { unique: true })
db.collection1.insert({ id: 1, value: 'hello' })
