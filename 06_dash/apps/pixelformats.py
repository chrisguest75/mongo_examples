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

df = pd.read_json('./data/imports_by_month_pixelformats.json')

def card():
    card = dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url('pixelformats.png'), top=True),
        dbc.CardBody(
            [
                html.H4("Pixel Formats", className="card-title"),
                html.P("Shows what our most pixel formats are over time",
                    className="card-text",
                ),
                dcc.Link(dbc.Button("Show", color="primary"), href='/apps/pixelformats'),
            ]
        ),
    ],
    style={"width": "18rem"},)
    return card

def dashboard():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("Imported Pixel Formats (grouped)", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("Shows what our most popular pixel formats are over time", className='mb-4'), width=12),),

        dbc.Row([
        dcc.Graph(id='app5-graph-with-slider'),
        ], align="center"),  # Vertical: start, center, end
        dbc.Row([
        dcc.Slider(
            id='app5-year-slider',
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
    Output('app5-graph-with-slider', 'figure'),
    Input('app5-year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.bar(filtered_df, x="month", y="total", color="pixel_format")

    fig.update_layout(transition_duration=500)

    return fig



    