from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import codecpopularity, bitratesheatmap, durationsstacked, resolutions, pixelformats, profiles, root


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/codecpopularity':
        return codecpopularity.page()
    elif pathname == '/apps/bitratesheatmap':
        return bitratesheatmap.page()
    elif pathname == '/apps/durationsstacked':
        return durationsstacked.page()
    elif pathname == '/apps/resolutions':
        return resolutions.page() 
    elif pathname == '/apps/pixelformats':
        return pixelformats.page()  
    elif pathname == '/apps/profiles':
        return profiles.page()                        
    else:
        return root.page([codecpopularity.card(), durationsstacked.card(), bitratesheatmap.card(), resolutions.card(), pixelformats.card(), profiles.card()])

if __name__ == '__main__':
    app.run_server(debug=True)

