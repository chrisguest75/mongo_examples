# README

Demonstrate how to connect `dash` to `mongo`

TODO:
 
* Add an index with a few different dashboards.  
* Add a month select split to the heatmap.  

* data has to be faked.  
* use tables, heatmaps, filters.. 

* heatmaps for sample and bitrate 
- https://plotly.com/python/2D-Histogram/
- https://plotly.com/python/heatmaps/
* number of audio streams in assets?


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
jsonsaver.saveJsonFile("./data/imports_by_month.json", out)
var out = tool.getImportsPerMonthCodecs()
jsonsaver.saveJsonFile("./data/imports_by_month_codecs.json", out)
var out = tool.getImportsPerMonthDurationGroup()
jsonsaver.saveJsonFile("./data/imports_by_month_durationgroups.json", out)
var out = tool.getImportsAudioRates()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates.json", out)
var out = tool.getImportsAudioRatesBuckets()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates_buckets.json", out)
var out = tool.getImportsAudioRatesBucketsYear()
jsonsaver.saveJsonFile("./data/imports_audio_bitrates_buckets_year.json", out)
```

## Render the dash chart

```sh
pipenv shell
code . 

# in terminal inside vscode
. ./.venv/bin/activate    

python ./imports-bubble.py     

python ./imports-codec-bubble.py       

python ./imports-duration-bubble.py       

python ./imports-duration-stacked.py

# use the bootstrap version of the codec bubble up
python ./imports-codec-bubble-bootstrap.py

# needs a bit of work
python ./imports-audiobitrates-heatmap.py 
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

https://stackoverflow.com/questions/68368745/logarithmic-heatmap-in-plotly