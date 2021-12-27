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

df = pd.read_json('./data/imports_by_month_durationgroups.json')

def dashboard():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("Imported Asset Durations (grouped)", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("Shows what our most popular durations are over time", className='mb-4'), width=12),),

        dbc.Row([
        dcc.Graph(id='app3-graph-with-slider'),
        ], align="center"),  # Vertical: start, center, end
        dbc.Row([
        dcc.Slider(
            id='app3-year-slider',
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
    Output('app3-graph-with-slider', 'figure'),
    Input('app3-year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.bar(filtered_df, x="month", y="total", color="duration_group")

    fig.update_layout(transition_duration=500)

    return fig



    