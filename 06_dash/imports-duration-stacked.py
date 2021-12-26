import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_json('./data/imports_by_month_durationgroups.json')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Imported Asset Durations (grouped)'),

    html.Div(children='''Breaks down duration into buckets per month'''),

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

    fig = px.bar(filtered_df, x="month", y="total", color="duration_group")

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

    