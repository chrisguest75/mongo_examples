function getDateRangeFiles() {
    const filesdb = db.getSiblingDB('d1')
    const files = filesdb.files.aggregate([
        {
          $match:
            {
              created: {
                $gte: ISODate(
                  "2023-12-14T12:00:00.000Z"
                ),
              },
            },
        },
        {
          $project:
            {
              created: 1,
              user: 1,
              item1_field1: {
                $arrayElemAt: [
                  "$myobject.myarray.field1",
                  0,
                ],
              },
              item2_field2: {
                $arrayElemAt: [
                  "$myobject.myarray.field2",
                  1,
                ],
              },
            },
        },
    ]).toArray();
    return files    
}

//console.log("Starting...")
var files = getDateRangeFiles()
console.log(JSON.stringify(files));

