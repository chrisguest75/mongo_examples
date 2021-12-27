import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from app import app
from apps import navbar

df = pd.read_json('./data/imports_by_month_codecs.json')
codecs_type = df[pd.notnull(df.codec_type)]
codecs_type = codecs_type['codec_type'].unique()
codecs_type.sort()
codecs = df[pd.notnull(df.codec_long_name)]
codecs = codecs['codec_long_name'].unique()
codecs.sort()

def card():
    card = dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url('codecs.png'), top=True),
        dbc.CardBody(
            [
                html.H4("Codecs", className="card-title"),
                html.P("Select Codec type and names to compare popularity over time.  Use to determine when the last time a codec was used.",
                    className="card-text",
                ),
                dcc.Link(dbc.Button("Show", color="primary"), href='/apps/codecpopularity'),
            ]
        ),
    ],
    style={"width": "18rem"},)
    return card


def dashboard():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H3("Imported Codec Popularity", className='mb-4'), width=12),),
        dbc.Row(dbc.Col(html.P("Select Codec type and names to compare popularity over time.  Use to determine when the last time a codec was used.", className='mb-4'), width=12),),
        
        dbc.Row([
            dbc.Col([
                dbc.Label("Type"),
                dcc.Dropdown(
                    id='app2-codecs-types-filter',
                    options=[{'label': i, 'value': i} for i in codecs_type],
                    multi=True,
                    searchable=True
                ),
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=6, xl=6
            ),
            dbc.Col([
                dbc.Label("Codec"),
                dcc.Dropdown(
                    id='app2-codecs-filter',
                    options=[{'label': i, 'value': i} for i in codecs],
                    multi=True,
                    searchable=True
                ),
                ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=6, xl=6
            ),

        ], justify='start'),  # Horizontal:start,center,end,between,around

        dbc.Row([
        dcc.Graph(id='app2-graph-with-slider'),
        ], align="center"),  # Vertical: start, center, end
        dbc.Row([
        dcc.Slider(
            id='app2-year-slider',
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
    dash.dependencies.Output('app2-codecs-filter', 'options'),
    [dash.dependencies.Input('app2-codecs-types-filter', 'value')])
def set_codecs_options(selected_types):
    if selected_types is not None:
        codecs = df[pd.notnull(df.codec_long_name)]

        # filter codecs on selected types
        filtered_df = codecs.loc[(codecs['codec_type'].isin(selected_types))]

        codecs = filtered_df['codec_long_name'].unique()
        codecs.sort()
    else:
        codecs = []
    return [{'label': i, 'value': i} for i in codecs]


@app.callback(
    Output('app2-graph-with-slider', 'figure'),
    Input('app2-year-slider', 'value'),
    Input('app2-codecs-filter', 'value'))
def update_figure(selected_year, codecs_filter):
    filtered_df = df[df.year == selected_year]
    print(codecs_filter)
    if codecs_filter is None:
        codecs_filter = []
    boolean_series = filtered_df.codec_long_name.isin(codecs_filter)
    codecfiltered_df = filtered_df[boolean_series]

    fig = px.scatter(codecfiltered_df, x="month", y="total",
                    size="total", color="codec_long_name", hover_name="total",
                    log_x=False, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

    