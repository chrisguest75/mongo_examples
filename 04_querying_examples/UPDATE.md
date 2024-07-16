# UPDATE

Working with modification.  

## Insert

```js
db.test.insertOne({
  item: 'canvas',
  qty: 100,
  tags: ['cotton', 'blue', 'red'],
  size: { h: 28, w: 35.5, uom: 'cm' } 
});

db.test.find();

db.test.updateOne({item:'canvas'}, {$set: {size: null}});

db.test.updateMany({item:'canvas'}, {$pull: {tags: 'blue'}});
```

## Resources

* db.collection.update() [here](https://www.mongodb.com/docs/manual/reference/method/db.collection.update/)
