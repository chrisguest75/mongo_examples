import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd


## TODO:
## * Bootstrap styling.


df = pd.read_json('./data/imports_by_month_codecs.json')
codecs_type = df[pd.notnull(df.codec_type)]
codecs_type = codecs_type['codec_type'].unique()
codecs_type.sort()
codecs = df[pd.notnull(df.codec_long_name)]
codecs = codecs['codec_long_name'].unique()
codecs.sort()


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Imported Codec Popularity'),

    html.Div(children='''Uses probe data to determine types of codec - you can multi-select codec types and codec used'''),
    html.Br(),
    html.Div([
        html.Div([
            html.Label([
                "type",
                    dcc.Dropdown(
                    id='codecs-types-filter',
                    options=[{'label': i, 'value': i} for i in codecs_type],
                    multi=True,
                    searchable=True
                ),
            ]),
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            html.Label([
                "codec",
                    dcc.Dropdown(
                    id='codecs-filter',
                    options=[{'label': i, 'value': i} for i in codecs],
                    multi=True,
                    searchable=True
                ),
            ]),
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='graph-with-slider'),
        ]),
            html.Div([
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].max(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ])
    ])
])

@app.callback(
    dash.dependencies.Output('codecs-filter', 'options'),
    [dash.dependencies.Input('codecs-types-filter', 'value')])
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
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    Input('codecs-filter', 'value'))
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


if __name__ == '__main__':
    app.run_server(debug=True)

    