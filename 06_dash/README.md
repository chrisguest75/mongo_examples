# README

Demonstrate how to connect `dash` to `mongo`

TODO:

* data has to be faked.  
* use tables, heatmaps, filters.. 

## Build and Run

To install locally you can clone the repo

```sh
pyenv install 3.9.0
pyenv local 3.9.0
export PIPENV_VENV_IN_PROJECT=1
pipenv install --pre --python $(pyenv which python)
```

## Export data from mongo into json

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"
use ffprobe  
load("./data/mongosh_imports_by_month.js");

var out = tool.getImportsPerMonth()
jsonsaver.saveImportsPerMonth("./data/imports_by_month.json", out)
var out = tool.getImportsPerMonthCodecs()
jsonsaver.saveImportsPerMonth("./data/imports_by_month_codecs.json", out)
var out = tool.getImportsPerMonthDurationGroup()
jsonsaver.saveImportsPerMonth("./data/imports_by_month_durationgroups.json", out)
```

## Render the dash chart

```sh
pipenv shell
code . 

# in terminal inside vscode
. ./.venv/bin/activate    

python ./imports-bubble.py     

# THIS IS NOT WORKING
python ./imports-codec-bubble.py       

python ./imports-duration-bubble.py       

```

## Resources

* [pyenv](https://github.com/pyenv/pyenv)  
* [pipenv](https://pypi.org/project/pipenv/)  
* Plot Live Graphs using Python Dash and Plotly [here](https://www.geeksforgeeks.org/plot-live-graphs-using-python-dash-and-plotly/)  
* Dash Installation [here](https://dash.plotly.com/installation)  
* plotly/jupyter-dash [repo](https://github.com/plotly/jupyter-dash)  
