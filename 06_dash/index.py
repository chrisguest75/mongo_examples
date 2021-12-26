from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import codecpopularity, bitratesheatmap, root


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/codecpopularity':
        return codecpopularity.layout
    elif pathname == '/apps/bitratesheatmap':
        return bitratesheatmap.layout
    else:
        return root.layout

if __name__ == '__main__':
    app.run_server(debug=True)
