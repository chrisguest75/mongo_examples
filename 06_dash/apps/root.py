from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Dashboard'),
    dcc.Link('Go to Codec Popularity', href='/apps/codecpopularity'),
    html.Br(),
    dcc.Link('Go to Bitrates Heatmap', href='/apps/bitratesheatmap')
])


    