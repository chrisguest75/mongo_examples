# README

Demonstrate how to connect `dash` to `mongo`

TODO:

* Convert it all to bootstrap
* Add a month select split to the heatmap.  
* data has to be faked.  
* use tables, filters.
* number of audio streams in assets?
* Resolutions? 
* Frame rates?
* pix_fmt?
* profile


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
# to manually export the data
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"
use ffprobe  
load("./data/mongosh_imports_by_month.js");

var out = tool.getImportsPerMonth()
jsonsaver.saveJsonFile("./data/imports_by_month.json", out)
```

```sh
# script will run and export data using mongosh and some scripts 
./export-dash-data.sh   
```

## Render the dash chart

```sh
pipenv shell
code . 

# in terminal inside vscode
. ./.venv/bin/activate    
```

### Multi Page

```sh
# an example multipage app
python ./index.py
```

### Single Pages

```sh
python ./singlepages/imports-bubble.py     

python ./singlepages/imports-codec-bubble.py       

python ./singlepages/imports-duration-bubble.py       

python ./singlepages/imports-duration-stacked.py

# use the bootstrap version of the codec bubble up
python ./singlepages/imports-codec-bubble-bootstrap.py

# needs a bit of work
python ./singlepages/imports-audiobitrates-heatmap.py 
```

## Create ico file

```sh
magick -density 128x128 -background none ./assets/favicon.png -resize 128x128 ./assets/favicon.ico
```

## Resources

* [pyenv](https://github.com/pyenv/pyenv)  
* [pipenv](https://pypi.org/project/pipenv/)  
* Plotly Python Open Source Graphing Library [here](https://plotly.com/python/)
* Plot Live Graphs using Python Dash and Plotly [here](https://www.geeksforgeeks.org/plot-live-graphs-using-python-dash-and-plotly/)  
* Dash Installation [here](https://dash.plotly.com/installation)  
* plotly/jupyter-dash [repo](https://github.com/plotly/jupyter-dash)  
* Dash Bootstrap Components [here](https://dash-bootstrap-components.opensource.faculty.ai/)  
* Coding-with-Adam/Dash-by-Plotly [repo](https://github.com/Coding-with-Adam/Dash-by-Plotly)  
* Multi-Page Apps and URL Support [here](https://dash.plotly.com/urls)  
* Logarithmic heatmap in Plotly [here](https://stackoverflow.com/questions/68368745/logarithmic-heatmap-in-plotly)  
* 2D Histograms in Python [here](https://plotly.com/python/2D-Histogram/)  
* Heatmaps in Python [here](https://plotly.com/python/heatmaps/)  


https://realpython.com/python-dash/


