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
        dbc.Row(dbc.Col(html.H3("ffprobe Analysis", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("A set of dashboards that can be used to analyse ffprobe data of a collection of media assets", className='mb-4'), width=12),),

        dbc.Row([
            dbc.Col([cards[0]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[1]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[2]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[3]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[4]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[5]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[6]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4, 
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),
            dbc.Col([cards[7]],# width={'size':5, 'offset':1, 'order':1},
            sm=6, lg=4,
            class_name="justify-content-center mb-3 d-flex align-items-stretch"
            ),

        ]),  # Horizontal:start,center,end,between,around
    ], fluid=True,)

    return layout

def page(cards):
    layout = dbc.Container([
        navbar.create_navbar(),
        dashboard(cards),
    ])

    return layout