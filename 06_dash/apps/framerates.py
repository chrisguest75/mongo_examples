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

df = pd.read_json('./data/imports_by_month_framerates.json')
codecs = df[pd.notnull(df.codec_long_name)]
codecs = codecs['codec_long_name'].unique()
codecs.sort()

def card():
    card = dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url('framerates.png'), top=True),
        dbc.CardBody(
            [
                html.H4("Framerates", className="card-title"),
                html.P("Investigate the most common framerates and associated codecs",
                    className="card-text mb-4 h-100",
                ),
                dcc.Link(dbc.Button("Show", color="primary", outline=True, class_name="w-100 mt-auto align-self-start"), href='/apps/framerates'),
            ], class_name="d-flex flex-column",
        ),
    ],
    style={"width": "18rem"},)
    return card

def dashboard():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("Imported Framerates (grouped)", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("Investigate the most common framerates and associated codecs", className='mb-4'), width=12),),

        dbc.Row([
            dbc.Col([
                dbc.Label("Codec"),
                dcc.Dropdown(
                    id='app7-codecs-filter',
                    options=[{'label': 'Select All', 'value': 'all_values'}] + [{'label': i, 'value': i} for i in codecs],
                    multi=True,
                    searchable=True
                ),
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=6, xl=6
            ),

        ], justify='start'),  # Horizontal:start,center,end,between,around

        dbc.Row([
        dcc.Graph(id='app7-graph-with-slider'),
        ], align="center"),  # Vertical: start, center, end
        dbc.Row([
        dcc.Slider(
            id='app7-year-slider',
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
    Output('app7-graph-with-slider', 'figure'),
    Input('app7-year-slider', 'value'),
    Input('app7-codecs-filter', 'value'))
def update_figure(selected_year, codecs_filter):
    filtered_df = df[df.year == selected_year]
    print(codecs_filter)
    if codecs_filter is None:
        codecs_filter = []
    boolean_series = filtered_df.codec_long_name.isin(codecs_filter)
    codecfiltered_df = filtered_df[boolean_series]

    if codecs_filter == ['all_values']:
        codecfiltered_df = filtered_df

    fig = px.bar(codecfiltered_df, x="month", y="total", color="frame_rate")

    fig.update_layout(transition_duration=500)

    return fig



    