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
codecs = df[pd.notnull(df.codec_long_name)]
codecs = codecs['codec_long_name'].unique()
codecs.sort()

print(widths)
print(heights)
print(codecs)

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
        dbc.Row(dbc.Col(html.P("Use the heatmap to see bandings of resolutions SD (720x576), HD (1280x720), Full-HD (1920x1080), UHD (3840x2160), 4K (4096x2160), 8K (7680×4320)", className='mb-4'), width=12),),

        dbc.Row([
            dbc.Col([
                dbc.Label("Codec"),
                dcc.Dropdown(
                    id='app4-codecs-filter',
                    options=[{'label': 'Select All', 'value': 'all_values'}] + [{'label': i, 'value': i} for i in codecs],
                    multi=True,
                    searchable=True
                ),
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=6, xl=6
            ),

        ], justify='start'),  # Horizontal:start,center,end,between,around

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
    Input('app4-year-slider', 'value'),
    Input('app4-codecs-filter', 'value'))
def update_figure(selected_year, codecs_filter):
    filtered_df = df[df.year == selected_year]
    print(codecs_filter)
    if codecs_filter is None:
        codecs_filter = []
    boolean_series = filtered_df.codec_long_name.isin(codecs_filter)
    codecfiltered_df = filtered_df[boolean_series]

    if codecs_filter == ['all_values']:
        codecfiltered_df = filtered_df

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

    for index, row in codecfiltered_df.iterrows():
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

    