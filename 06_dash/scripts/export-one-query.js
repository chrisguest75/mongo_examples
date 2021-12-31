load("./scripts/mongosh_imports_by_month.js");

print('getImportsPixelFormatsYear()\n==============================\n');
var out = tool.getImportsPixelFormatsYear()
jsonsaver.saveJsonFile("./data/imports_by_month_pixelformats.json", out)

