load("./scripts/mongosh_imports_by_month.js");

print('getImportsPerMonth()\n==============================\n');
var out = tool.getImportsPerMonth()
jsonsaver.saveJsonFile("./data/imports_by_month.json", out)

print('getImportsPerMonthCodecs()\n==============================\n');
var out = tool.getImportsPerMonthCodecs()
jsonsaver.saveJsonFile("./data/imports_by_month_codecs.json", out)

print('getImportsPerMonthDurationGroup()\n==============================\n');
var out = tool.getImportsPerMonthDurationGroup()
jsonsaver.saveJsonFile("./data/imports_by_month_durationgroups.json", out)

print('getImportsAudioRates()\n==============================\n');
var out = tool.getImportsAudioRates()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates.json", out)

print('getImportsAudioRatesBuckets()\n==============================\n');
var out = tool.getImportsAudioRatesBuckets()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates_buckets.json", out)

print('getImportsAudioRatesBucketsYear()\n==============================\n');
var out = tool.getImportsAudioRatesBucketsYear()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates_buckets_year.json", out)

