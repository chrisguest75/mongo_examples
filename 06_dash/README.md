# README

Demonstrate how to connect `dash` to `mongo`

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
python ./bubble.py       
```

## Resources

* [pyenv](https://github.com/pyenv/pyenv)  
* [pipenv](https://pypi.org/project/pipenv/)  
* Plot Live Graphs using Python Dash and Plotly [here](https://www.geeksforgeeks.org/plot-live-graphs-using-python-dash-and-plotly/)  


https://dash.plotly.com/installation
https://github.com/plotly/jupyter-dash

