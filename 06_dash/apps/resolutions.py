import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

import pandas as pd
import numpy as np
from app import app
from apps import navbar

viridis = px.colors.sequential.Viridis

#df = pd.read_json("./data/imports_audio_bitrates.json")
df = pd.read_json("./data/imports_resolutions_year.json")
widths = df[pd.notnull(df.xresolution)]
widths = widths['xresolution'].unique()
widths.sort()
heights = df[pd.notnull(df.yresolution)]
heights = heights['yresolution'].unique()
heights.sort()

print(widths)
print(heights)

def card():
    card = dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url('resolutions.png'), top=True),
        dbc.CardBody(
            [
                html.H4("Resolutions", className="card-title"),
                html.P("What are the most common resolutions?",
                    className="card-text",
                ),
                dcc.Link(dbc.Button("Show", color="primary"), href='/apps/resolutions'),
            ]
        ),
    ],
    style={"width": "18rem"},)
    return card

# zdata = { 'z': data }
def dashboard():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("Resolutions Heatmap", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("Use the heatmap ", className='mb-4'), width=12),),

        dbc.Row([
        dcc.Graph(id='app4-graph-with-slider'),
        ], align="center"),  # Vertical: start, center, end
        dbc.Row([
        dcc.Slider(
            id='app4-year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].max(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )
        ], align="center"),  # Vertical: start, center, end
    ], fluid=True)
    return layout

def page():
    layout = dbc.Container([
        navbar.create_navbar(),
        dashboard(),
    ])

    return layout


@app.callback(
    Output('app4-graph-with-slider', 'figure'),
    Input('app4-year-slider', 'value'))
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
    for y in range(0, len(heights)):
        row = []
        for x in range(0, len(widths)):
            row.append(0)
        data.append(row)

    for index, row in filtered_df.iterrows():
        x = np.where(widths == row['xresolution'])[0].min()
        y = np.where(heights == row['yresolution'])[0].min()
        data[y][x] += int(row['total'])

    print(data)

    fig = px.imshow(data,
                    labels=dict(x="xresolution", y="yresolution", color="total"),
                    x=widths,
                    y=heights,
                    color_continuous_scale=colorscale,
                    text_auto=True, aspect="auto"
                )
    fig.update_xaxes(side="top")

    return fig

    