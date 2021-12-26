import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import numpy as np

viridis = px.colors.sequential.Viridis

#df = pd.read_json("./data/imports_audio_bitrates.json")
df = pd.read_json("./data/imports_audio_bitrates_buckets.json")
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
# zdata = { 'z': data }

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Bitrates Heatmap (grouped - logplot)'),

    html.Div(children='''Show most common bitrates and samplerates (log plot)'''),

    html.Div([
        html.Div([
            dcc.Graph(id='graph-with-slider'),
        ]),
            html.Div([
            dcc.Slider(
                id='year-slider',
                min=0,
                max=10,
                value=5,
                marks={str(year): str(year) for year in range(0,10)},                step=None
            )
        ])
    ])
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    colorscale = [
            [0, viridis[0]],
            [1./1000000, viridis[2]],
            [1./10000, viridis[4]],
            [1./100, viridis[7]],
            [1., viridis[9]],
    ]
    # fig = px.density_heatmap(x=df['bit_rate'], y=df['sample_rate'],z=df['total'], color_continuous_scale=colorscale)

    fig = px.imshow(data,
                    labels=dict(x="Bitrates", y="Samplerates", color="total"),
                    x=bitrates,
                    y=samplerates,
                    color_continuous_scale=colorscale,
                    text_auto=True, aspect="auto"
                )
    fig.update_xaxes(side="top")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

    