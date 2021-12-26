let error = false

let res = [
  db.test.drop(),
  db.createUser(
    {
      user: "test",
      pwd: "testpassword",
      roles: [ { role: "readWrite", db: "test" } ]
    }
  ),  
  db.test.createIndex({ id: 1 }, { unique: true }),
  db.test.insert({ id: 1, value: 'hello' }),

  // ffprobe data
  db.createUser(
    {
      user: "ffprobe",
      pwd: "ffprobepassword",
      roles: [ { role: "readWrite", db: "ffprobe" } ]
    }
  ),  

]

printjson(res)


if (error) {
  print('Error occured during initialisation')
  quit(1)
}