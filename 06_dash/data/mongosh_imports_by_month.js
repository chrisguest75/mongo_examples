/*```csv
codec,year,month,imports,type,duration
AAC,2020,Dec,600,Audio,900
```*/
var tool = (function () {
    return {
        getImportsPerMonth: function () {
            print('\nImports\n==============================');
      
            var importsArray = db.getCollection('prod').aggregate([
                { $project : { created: { $ifNull: [ "$created", new Date("2000-01-01T00:00:00Z") ] } } },
                { $project : { month_num : {$month : { $toDate: "$created"  }}, year : {$year :  { $toDate: "$created"  }},}},
                { $project : { 
                    month: {
                        $let: {
                            vars: {
                                monthsInString: [, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                            },
                            in: {
                                $arrayElemAt: ['$$monthsInString', '$month_num']
                            }
                        }
                    }, 
                    year: 1,
                    month_num: 1
                } },    
                { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num", }, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", total:"$total" }}}},
                { $sort : { _id : 1}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", total:"$months.total"}}, 
                { $sort : { year : 1, month_num: 1}},
            
             ]).toArray(); 
            //printjson(importsArray);
            return importsArray
        },
        getImportsPerMonthCodecs: function () {
            print('\nImports\n==============================');
      
            var importsArray = db.getCollection('prod').aggregate([
                { $project : { probe: 1, created: { $ifNull: [ "$created", new Date("2000-01-01T00:00:00Z") ] } } },
                { $project : { probe: 1, month_num : {$month : { $toDate: "$created"  }}, year : {$year :  { $toDate: "$created"  }},}},
                { $project : { 
                    month: {
                        $let: {
                            vars: {
                                monthsInString: [, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                            },
                            in: {
                                $arrayElemAt: ['$$monthsInString', '$month_num']
                            }
                        }
                    }, 
                    year: 1,
                    month_num: 1,
                    probe: 1,
                } },    
                { $unwind: '$probe.streams' },
                { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num", codec_type : "$probe.streams.codec_type", codec_long_name : "$probe.streams.codec_long_name"}, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", codec_type : "$_id.codec_type", codec_long_name : "$_id.codec_long_name", total : "$total" }}}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", codec_type : "$months.codec_type", codec_long_name : "$months.codec_long_name", total:"$months.total"}}, 
                  { $sort : { year : 1, month_num: 1}},
             ]).toArray(); 
            //printjson(importsArray);
            return importsArray
        }

    }
})();

var jsonsaver = (function () {
    return {
        saveImportsPerMonth: function (filepath, data) {
            print("Saving " + filepath);
            var outjson = JSON.stringify(data);
            fs.writeFile(filepath, outjson, function (err) {
                if (err) {
                    print('Saving failed');    
                }
            });            
        }
    }
})();

