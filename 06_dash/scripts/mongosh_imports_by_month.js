
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
        },
        getImportsPerMonthDurationGroup: function () {
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
                    { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num", "duration_group": {
                        "$cond": [
                            { "$lt": [ { $toDouble:"$probe.streams.duration" } , 10 ] },
                            "(1) 0-10secs",
                                {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.duration"}, 60 ] },
                            "(2) 10-60secs",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.duration"}, 600 ] },
                            "(3) 60-600secs",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.duration"}, 3600 ] },
                            "(4) 600-3600secs",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.duration"}, 7200 ] },
                            "(5) 3600-7200secs",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.duration"}, 10800 ] },
                            "(6) 7200-10800secs",
                            "(7) 10800+secs"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
            
                      ]
                    },
                        }, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", duration_group : "$_id.duration_group", total : "$total" }}}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", duration_group : "$months.duration_group", total:"$months.total"}}, 
                  { $sort : { year : 1, month_num: 1, duration_group: 1 }},
            ]).toArray(); 
            //printjson(importsArray);
            return importsArray
        },
        getImportsAudioRates: function () {
            print('\nImports\n==============================');
            var importsArray = db.getCollection('prod').aggregate([
                { $unwind: '$probe.streams' },
                { $match: {'probe.streams.codec_type': 'audio'} },
                
                { $project: { _id: 0, codec_long_name:{ $toString:"$probe.streams.codec_long_name" }, sample_rate: "$probe.streams.sample_rate", bit_rate: {
                        "$cond": [
                            { "$lt": [ { $toDouble:"$probe.streams.bit_rate" } , 10000 ] },
                            "(1) <10000bps",
                                {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 20000 ] },
                            "(2) 10000-20000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 40000 ] },
                            "(3) 20000-40000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 80000 ] },
                            "(4) 40000-80000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 160000 ] },
                            "(5) 80000-160000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 320000 ] },
                            "(6) 160000-320000bps",
                            "(7) >320000bps"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                    },
                    },    
                { $group : { _id :  { codec_long_name: "$codec_long_name", sample_rate: "$sample_rate", bit_rate:"$bit_rate", }, total: { $sum : 1 } }},
                {$project: { _id: 0, codec_long_name:"$_id.codec_long_name", sample_rate:"$_id.sample_rate", bit_rate:"$_id.bit_rate", total : "$total"}}, 
                  { $sort : { codec_long_name : 1}},
                        ]).toArray(); 
        //printjson(importsArray);
            return importsArray            
        },
        getImportsAudioRatesBuckets: function () {
            print('\nImports\n==============================');
            var importsArray = db.getCollection('prod').aggregate([
                { $unwind: '$probe.streams' },
                { $match: {'probe.streams.codec_type': 'audio'} },
                
                { $project: { _id: 0, codec_long_name:{ $toString:"$probe.streams.codec_long_name" }, sample_rate: {
                        "$cond": [
                            { "$lte": [ { $toDouble:"$probe.streams.sample_rate" } , 4000 ] },
                            "(1) <4000hz",
                                {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 8000 ] },
                            "(2) 4000-8000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 12000 ] },
                            "(3) 8000-12000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 16000 ] },
                            "(4) 12000-16000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 32000 ] },
                            "(5) 16000-32000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 48000 ] },
                            "(6) 320000-48000hz",
                            "(7) >48000hz"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                 bit_rate: {
                        "$cond": [
                            { "$lt": [ { $toDouble:"$probe.streams.bit_rate" } , 10000 ] },
                            "(1) <10000bps",
                                {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 20000 ] },
                            "(2) 10000-20000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 40000 ] },
                            "(3) 20000-40000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 80000 ] },
                            "(4) 40000-80000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 160000 ] },
                            "(5) 80000-160000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 320000 ] },
                            "(6) 160000-320000bps",
                            "(7) >320000bps"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                    },
                },    
                { $group : { _id :  { codec_long_name: "$codec_long_name", sample_rate: "$sample_rate", bit_rate:"$bit_rate", }, total: { $sum : 1 } }},
                {$project: { _id: 0, codec_long_name:"$_id.codec_long_name", sample_rate:"$_id.sample_rate", bit_rate:"$_id.bit_rate", total : "$total"}}, 
                  { $sort : { codec_long_name : 1}},
        ]).toArray(); 
        //printjson(importsArray);
            return importsArray            
        },
        getImportsAudioRatesBucketsYear: function () {
            print('\nImports\n==============================');
            var importsArray =  db.getCollection('prod').aggregate([
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
                { $match: {'probe.streams.codec_type': 'audio'} },
                
                { $project: { _id: 0, year: "$year", month: "$month", month_num:"$month_num", codec_long_name:{ $toString:"$probe.streams.codec_long_name" }, sample_rate: {
                        "$cond": [
                            { "$lte": [ { $toDouble:"$probe.streams.sample_rate" } , 4000 ] },
                            "(1) <4000hz",
                                {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 8000 ] },
                            "(2) 4000-8000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 12000 ] },
                            "(3) 8000-12000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 16000 ] },
                            "(4) 12000-16000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 32000 ] },
                            "(5) 16000-32000hz",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.sample_rate"}, 48000 ] },
                            "(6) 320000-48000hz",
                            "(7) >48000hz"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                 bit_rate: {
                        "$cond": [
                            { "$lt": [ { $toDouble:"$probe.streams.bit_rate" } , 10000 ] },
                            "(1) <10000bps",
                                {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 20000 ] },
                            "(2) 10000-20000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 40000 ] },
                            "(3) 20000-40000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 80000 ] },
                            "(4) 40000-80000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 160000 ] },
                            "(5) 80000-160000bps",
                            {"$cond": [
                            { "$lt": [ {$toDouble:"$probe.streams.bit_rate"}, 320000 ] },
                            "(6) 160000-320000bps",
                            "(7) >320000bps"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                    },
                },    
                { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num",  codec_long_name: "$codec_long_name", sample_rate: "$sample_rate", bit_rate:"$bit_rate",}, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", codec_long_name: "$_id.codec_long_name", sample_rate: "$_id.sample_rate", bit_rate:"$_id.bit_rate", total : "$total" }}}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", codec_long_name : "$months.codec_long_name", sample_rate : "$months.sample_rate", bit_rate : "$months.bit_rate", total:"$months.total"}}, 
                  { $sort : { year : 1, month_num: 1}},                       
        ]).toArray(); 
        //printjson(importsArray);
            return importsArray            
        },
        getImportsResolutionsYear: function () {
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
                { $match: {'probe.streams.codec_type': 'video'} },
                
                { $project: { _id: 0, year: "$year", month: "$month", month_num:"$month_num", codec_long_name:{ $toString:"$probe.streams.codec_long_name" }, xresolution: {
                        "$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width" }, 720 ] },
                            "(1) SD",
                                {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width"}, 1280 ] },
                            "(2) HD",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width"}, 1920 ] },
                            "(3) Full-HD",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width"}, 3840 ] },
                            "(4) UHD",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width"}, 4096 ] },
                            "(5) 4K",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.width"}, 7680 ] },
                            "(6) 8K",
                            "(7) >8K"
                        ]}
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    }, yresolution: {
                        "$cond": [
                            { "$lte": [ { $toDouble:"$probe.streams.height" } , 576 ] },
                            "(1) SD",
                                {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.height"}, 720 ] },
                            "(2) HD",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.height"}, 1080 ] },
                            "(3) Full-HD",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.height"}, 2160 ] },
                            "(4) UHD/4K",
                            {"$cond": [
                            { "$lte": [ {$toDouble:"$probe.streams.height"}, 4320 ] },
                            "(5) 8K",
                            "(6) >8K"
                        ]}
                        ]}                
                        ]}
                        ]}
                      ]
                    },
                    },
                },    
                { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num",  codec_long_name: "$codec_long_name", xresolution: "$xresolution", yresolution: "$yresolution",}, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", codec_long_name: "$_id.codec_long_name", xresolution: "$_id.xresolution", yresolution: "$_id.yresolution", total : "$total" }}}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", codec_long_name : "$months.codec_long_name", xresolution : "$months.xresolution", yresolution : "$months.yresolution", total:"$months.total"}}, 
                  { $sort : { year : 1, month_num: 1}},                       
        ]).toArray(); 
        //printjson(importsArray);
            return importsArray            
        },
        getImportsPixelFormatsYear: function () {
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
                { $match: {'probe.streams.codec_type': 'video'} },
                { $group : { _id :  { year: "$year", month: "$month", month_num:"$month_num", pixel_format : { $ifNull: [ "$probe.streams.pix_fmt", "UNKNOWN" ] } }, total: { $sum : 1 } }},
                { $group : { _id :  "$_id.year", months: { $push: { month:"$_id.month", month_num:"$_id.month_num", pixel_format : "$_id.pixel_format", total : "$total" }}}},
                {$unwind:"$months"},
                {$project: {year:"$_id", month:"$months.month", month_num:"$months.month_num", pixel_format : "$months.pixel_format", total:"$months.total"}}, 
                  { $sort : { year : 1, month_num: 1}},
             ]).toArray(); 
            //printjson(importsArray);
            return importsArray            
        },            
    }
})();














var jsonsaver = (function () {
    return {
        saveJsonFile: function (filepath, data) {
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

