import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

import pandas as pd
import numpy as np
from app import app

viridis = px.colors.sequential.Viridis

#df = pd.read_json("./data/imports_audio_bitrates.json")
df = pd.read_json("./data/imports_audio_bitrates_buckets_year.json")
bitrates = df[pd.notnull(df.bit_rate)]
bitrates = bitrates['bit_rate'].unique()
bitrates.sort()
samplerates = df[pd.notnull(df.sample_rate)]
samplerates = samplerates['sample_rate'].unique()
samplerates.sort()

print(samplerates)
print(bitrates)

# zdata = { 'z': data }

layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Bitrates Heatmap (grouped - logplot)",
                        className='text-center text-primary mb-4'),
                width=12),
    ),

    dbc.Row([
    dcc.Graph(id='app1-graph-with-slider'),
    ], align="center"),  # Vertical: start, center, end
    dbc.Row([
    dcc.Slider(
        id='app1-year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].max(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
    ], align="center"),  # Vertical: start, center, end
    dbc.Row([
         dcc.Link('Go to Root', href='/')
    ], align="center"),
], fluid=True)



@app.callback(
    Output('app1-graph-with-slider', 'figure'),
    Input('app1-year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    colorscale = [
            [0, viridis[0]],
            [1./1000000, viridis[2]],
            [1./10000, viridis[4]],
            [1./100, viridis[7]],
            [1., viridis[9]],
    ]
    # fig = px.density_heatmap(x=df['bit_rate'], y=df['sample_rate'],z=df['total'], color_continuous_scale=colorscale)
    data=[]
    for y in range(0, len(samplerates)):
        row = []
        for x in range(0, len(bitrates)):
            row.append(0)
        data.append(row)

    for index, row in filtered_df.iterrows():
        x = np.where(bitrates == row['bit_rate'])[0].min()
        y = np.where(samplerates == row['sample_rate'])[0].min()
        data[y][x] += int(row['total'])

    print(data)

    fig = px.imshow(data,
                    labels=dict(x="Bitrates", y="Samplerates", color="total"),
                    x=bitrates,
                    y=samplerates,
                    color_continuous_scale=colorscale,
                    text_auto=True, aspect="auto"
                )
    fig.update_xaxes(side="top")

    return fig

    