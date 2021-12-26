db.newdb.drop()
db.createUser(
{
    user: "newdb",
    pwd: "newdbpassword",
    roles: [ { role: "readWrite", db: "newdb" } ]
}
)
db.newdb.createIndex({ id: 1 }, { unique: true })
db.newdb.insert({ id: 1, value: 'hello' })
