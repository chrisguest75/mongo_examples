# AGGREGATIONS

TODO:

* How do I join with a date dimension to zero out days with no data?  https://www.mongodb.com/blog/post/introducing-gap-filling-time-series-data-mongodb-5-3

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

Match documents then count. Have to use [ISODate](https://en.wikipedia.org/wiki/ISO_8601) for ranges.  

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

## Aggregate by day

```sh
[
  {
    $match: {
      created: {
        $gt: ISODate("2023-05-1"),
        $lt: ISODate("2023-05-19"),
      },
    },
  },
  {
    $project: {
      day: {
        $dayOfMonth: { $toDate: "$created" },
      },
      month_num: {
        $month: { $toDate: "$created" },
      },
      year: { $year: { $toDate: "$created" } },
    },
  },
  {
    $group: {
      _id: {
        year: "$year",
        month: "$month",
        month_num: "$month_num",
        day: "$day",
      },
      total: { $sum: 1 },
    },
  },
  {
    $project: {
      year: "$_id.year",
      month: "$_id.month_num",
      day: "$_id.day",
      total: "$total",
    },
  },
  { $sort: { year: 1, month_num: 1, day: 1 } },
]
```
