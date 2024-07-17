# JOINS

Joining data from different collections can be achieved in the aggregation framework.  

## Contents

- [JOINS](#joins)
  - [Contents](#contents)
  - [Lookup](#lookup)

## Lookup

Books array contains ids for book in books collection. Create a new array replacing the ids with title and price.  

```json
    {
      $lookup: {
        from: "books",
        localField: "ids",
        foreignField: "_id",
        as: "books"
      }
    },
    {
      $project: {
         books: {
          $map: {
            input: "$books",
            as: "book",
            in: {
              $concat: ["$$book.title", " - ", "$$book.price"]
            }
          }
        }
      }
    }
  ]
```

