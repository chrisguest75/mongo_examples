# README

Demonstrate how to connect `dash` to `mongo`

TODO:

* data has to be faked.  
* use tables, filters.
* number of audio streams in assets?
* trancoding statuses by codec and time.  

## Build and Run

To install locally you can clone the repo

```sh
pyenv install 3.9.0
pyenv local 3.9.0
export PIPENV_VENV_IN_PROJECT=1
pipenv install --pre --python $(pyenv which python)
```

## Render the dash chart

```sh
pipenv shell
code . 

# in terminal inside vscode
. ./.venv/bin/activate    

# an example multipage app
python ./index.py
```

## Multipage code

All dashboards have a very similar structure.  

Code is structured with a untyped interface.  Each module has a card() and page() used for creating markup.  
card() is used for the index page and the page() is used to render the dashboard itself.  

## Add a new dashboard

1) Copy an existing dashbaord python file to a `new_dashboard.py`
2) Add import and add a new card to the `index.py` file.  
3) Add the aggregation query to the `./scripts/mongosh_imports_by_month.js` file in a function.  
4) Add the route to the `./apps/navbar.py` file  
5) Add a new card to the grid `./apps/root.py`. The array is passed into the root page from `index.py`
6) In `new_dashboard.py` we need to ensure the labels for the controls are unique across the whole project.  


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

## Export data from mongo into json

Data is created by the `ffprobe` example [here](../03_ffprobe/README.md)  

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
* Develop Data Visualization Interfaces in Python With Dash [here](https://realpython.com/python-dash/)
* How to Create a Multipage Dash App [here](https://medium.com/@mcmanus_data_works/how-to-create-a-multipage-dash-app-75c2ddb79315)
* dash-bootstrap-components Themes [here](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
