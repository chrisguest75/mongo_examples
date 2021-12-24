# README

Demonstrate how to connect `dash` to `mongo`

TODO:

* data has to be faked.  

## Build and Run

To install locally you can clone the repo

```sh
pyenv install 3.9.0
pyenv local 3.9.0
export PIPENV_VENV_IN_PROJECT=1
pipenv install --pre --python $(pyenv which python)
```

```sh
pipenv shell
code . 

# in terminal inside vscode
. ./.venv/bin/activate    

python ./main.py   
python ./imports_bubble.py       
```


```csv
codec,year,month,imports,type,duration
AAC,2020,Dec,600,Audio,900
```

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"  
load("./data/mongosh_imports_by_month.js");
use ffprobe
var out = tool.getImportsPerMonth()
jsonsaver.saveImportsPerMonth("./data/imports_by_month.json", out)
```

## Resources

* [pyenv](https://github.com/pyenv/pyenv)  
* [pipenv](https://pypi.org/project/pipenv/)  
* Plot Live Graphs using Python Dash and Plotly [here](https://www.geeksforgeeks.org/plot-live-graphs-using-python-dash-and-plotly/)  


https://dash.plotly.com/installation
https://github.com/plotly/jupyter-dash

