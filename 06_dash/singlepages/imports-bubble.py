import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_json('./data/imports_by_month.json')
#df = pd.read_json('./data/imports_by_month_codecs.json')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Imported files'),

    html.Div(children='''Counts of raw imports month-by-month.  Use `slider` to select year'''),

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
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="month", y="total",
                     size="total", color="month", hover_name="month",
                     log_x=False, size_max=55)

    # fig = px.scatter(filtered_df, x="codec_long_name", y="total",
    #                 size="total", color="codec_type", hover_name="codec_long_name",
    #                 log_x=False, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

    