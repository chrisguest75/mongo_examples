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
                    dbc.DropdownMenuItem("Resolutions", href='/apps/resolutions'),
                    dbc.DropdownMenuItem("Durations ", href='/apps/durationsstacked'),
                    dbc.DropdownMenuItem("Pixel Formats", href='/apps/pixelformats'),
                    dbc.DropdownMenuItem("Profiles", href='/apps/profiles'),
                    dbc.DropdownMenuItem("Framerates", href='/apps/framerates'),
                    dbc.DropdownMenuItem("Status", href='/apps/status'),
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
    