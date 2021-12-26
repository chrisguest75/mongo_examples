let error = false

let res = [
  db.createUser(
    {
      user: "startup",
      pwd: "startuppassword",
      roles: [ { role: "readWrite", db: "startup" } ]
    }
  ),  
  db.startup.createIndex({ id: 1 }, { unique: true }),
  db.startup.insert({ id: 1, value: 'hello' }),
]

printjson(res)


if (error) {
  print('Error occured during initialisation')
  quit(1)
}