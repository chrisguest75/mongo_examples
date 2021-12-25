import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import numpy as np

df = pd.read_json("./data/imports_audio_bitrates.json")
bitrates = df[pd.notnull(df.bit_rate)]
bitrates = bitrates['bit_rate'].unique()
bitrates.sort()
samplerates = df[pd.notnull(df.sample_rate)]
samplerates = samplerates['sample_rate'].unique()
samplerates.sort()

print(samplerates)
print(bitrates)

data=[]
for y in range(0, len(samplerates)):
    row = []
    for x in range(0, len(bitrates)):
        row.append(0)
    data.append(row)

for index, row in df.iterrows():
    x = np.where(bitrates == row['bit_rate'])[0].min()
    y = np.where(samplerates == row['sample_rate'])[0].min()
    data[y][x] += int(row['total'])

print(data)

#data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
    id='year-slider',
    min=0,
    max=10,
    value=5,
    marks={str(year): str(year) for year in range(0,10)},
    step=None
)
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):

    fig = px.imshow(data,
                    labels=dict(x="Bitrates", y="Samplerates", color="Productivity"),
                    x=bitrates,
                    y=samplerates,
                    text_auto=True
                )
    fig.update_xaxes(side="top")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

    