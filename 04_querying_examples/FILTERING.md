# Filtering Examples

```js
// works on mongo v5
db.files.find({"status":{ $ne: "complete" }, "created" : { $gte : new ISODate("2021-12-20T00:00:000Z") }});

// works on mongo v4
db.getCollection('files').find({"status":{ $ne: "complete" }, "created" : { $gte : new ISODate("2021-12-20T00:00") }});
```



## Resources

