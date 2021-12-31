load("./scripts/mongosh_imports_by_month.js");

print('getImportsFrameRatesYear()\n==============================\n');
var out = tool.getImportsFrameRatesYear()
jsonsaver.saveJsonFile("./data/imports_by_month_framerates.json", out)
