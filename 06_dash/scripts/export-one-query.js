load("./scripts/mongosh_imports_by_month.js");

print('getImportsStatusYear()\n==============================\n');
var out = tool.getImportsStatusYear()
jsonsaver.saveJsonFile("./data/imports_by_month_status.json", out)
