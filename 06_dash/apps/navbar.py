import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.Container([
        dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Codecs", href='/apps/codecpopularity'),
                    dbc.DropdownMenuItem("Bitrates", href='/apps/bitratesheatmap'),
                    dbc.DropdownMenuItem("Durations ", href='/apps/durationsstacked'),
                ],
            ),
        ],
        brand="Home",
        brand_href="/",
        sticky="top",
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    ),
    ])

    return navbar
    