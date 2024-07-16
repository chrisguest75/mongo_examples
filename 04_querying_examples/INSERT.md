# INSERT

Working with insertions.  

## Insert

```js
db.test.insertOne({
  item: 'canvas',
  qty: 100,
  tags: ['cotton', 'blue', 'red'],
  size: { h: 28, w: 35.5, uom: 'cm' } 
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

* Insert Documents [here](https://www.mongodb.com/docs/manual/tutorial/insert-documents/)
