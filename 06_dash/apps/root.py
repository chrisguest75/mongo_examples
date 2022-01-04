from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps import navbar

from app import app

## TODO:
## Fill the columns in dynamically

def dashboard(cards):
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("FFProbe Analysis", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("A set of dashboards that can be used to analyse ffprobe data for input assets", className='mb-4'), width=12),),

        dbc.Row([
            dbc.Col([
                    cards[0]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
            dbc.Col([
                    cards[1]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
            dbc.Col([
                    cards[2]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
        ], justify='start'),  # Horizontal:start,center,end,between,around
        dbc.Row([
            dbc.Col([
                    cards[3]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
            dbc.Col([
                    cards[4]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
            dbc.Col([
                    cards[5]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
        ], justify='start'),  # Horizontal:start,center,end,between,around
        dbc.Row([
            dbc.Col([
                    cards[6]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),
            dbc.Col([
                    cards[7]
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=6, sm=6, md=6, lg=4, xl=4
            ),

        ], justify='start'),  # Horizontal:start,center,end,between,around
    ], fluid=True)

    return layout

def page(cards):
    layout = dbc.Container([
        navbar.create_navbar(),
        dashboard(cards),
    ])

    return layout