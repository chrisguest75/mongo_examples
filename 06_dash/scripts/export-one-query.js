load("./scripts/mongosh_imports_by_month.js");

print('getImportsResolutionsYear()\n==============================\n');
var out = tool.getImportsResolutionsYear()
jsonsaver.saveJsonFile("./data/imports_resolutions_year.json", out)

