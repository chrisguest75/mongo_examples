# AGGREGATIONS

## Unique values

Unique values in a field.

```json
[
  {
    $group: {
      _id: "$myField",
    },
  },
  {
    $project:
      {
        myField: 1
      },
  },
]
```

## Count documents in date range

Have to use ISODate for ranges.  

```json
[
  {
    $match: {
      created: {
        $gt: ISODate("2023-05-05"),
        $lt: ISODate("2023-05-06"),
      },
      duration: {
        $gt: 0,
      },
      myField: "myValue",
    },
  },
  {
    $count:
      "string",
  },
]
```

## Where a field exists and is set

```json
[
  {
    $match: {
      created: {
        $gt: ISODate("2023-05-09"),
        $lt: ISODate("2023-05-10"),
      },
    $expr: {
        $and: [
          { $ne: ["$myField", null] },
          { $ne: ["$myField", undefined] }
        ]
      }      
    },
  }
]
```

## Difference between created and updated

```json
[
  {
    $match: {
      created: {
        $gt: ISODate("2023-05-09"),
        $lt: ISODate("2023-05-10"),
      },
    },
  },
  {
    $addFields:
      {
        time_difference_in_minutes: {
          $divide: [
            {
              $subtract: ["$updated", "$created"],
            },
            1000 * 60, // Divide by milliseconds per minute
          ],
        },
      },
  },
  {
    $project:
      {
        Id: 1, time_difference_in_minutes:1, created: 1
      },
  },
]
```
