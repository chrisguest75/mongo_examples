from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps import navbar

from app import app

def dashboard():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.H1("ffprobe Dashboard",
                            className='text-primary mb-4'),
                    width=12)
        ),

        dbc.Row([

            dbc.Col([
                    dcc.Link('Go to Codec Popularity', href='/apps/codecpopularity'),
                    html.Br(),
                    dcc.Link('Go to Bitrates Heatmap', href='/apps/bitratesheatmap'),
                    html.Br(),
                    dcc.Link('Go to Duration Stacked', href='/apps/durationsstacked')
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5
            ),

        ], justify='start'),  # Horizontal:start,center,end,between,around

    ], fluid=True)

    return layout

def page():
    layout = dbc.Container([
        navbar.create_navbar(),
        dashboard(),
    ])

    return layout