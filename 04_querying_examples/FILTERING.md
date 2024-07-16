# Filtering Examples

Working with query filtering.  

## Find

```js
// works on mongo v5
db.files.find({
    "status":{ $ne: "complete" }, 
    "created" : { $gte : new ISODate("2021-12-20T00:00:000Z") }
});

// works on mongo v4
db.getCollection('files').find({
    "status":{ $ne: "complete" }, 
    "created" : { $gte : new ISODate("2021-12-20T00:00") }
});
```

## Projection

```js
// works on mongo v5
db.files.find({
    "status":{ $ne: "complete" }, 
    "created" : { $gte : new ISODate("2021-12-20T00:00:000Z") }
},
{   
    "name": 1,
    "created": 1,
}
);
```

## Resources

* db.collection.find() [here](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/)
