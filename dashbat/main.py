import argparse
from ipaddress import ip_address

import plotly.express as px

import dash
from dash.dependencies import Output, Input
from dash.development.base_component import Component
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from dashbat.data.data_types import DATASET_NAMES, DatasetName
import dashbat.figures as dfig


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)


def _theme_dropdown() -> Component:
    options = [{"value": id_, "label": name} for id_, name in DATASET_NAMES.items()]
    return dcc.Dropdown(
        id="theme-dropdown", options=options, value="transition", className="my-3"
    )


def _column_dropdown() -> Component:
    options = [
        {"value": column, "label": column}
        for column in ["Nombre contributions", "Contributions 1 000 habitants"]
    ]

    return dcc.Dropdown(
        id="display-column-dropdown",
        options=options,
        value="Nombre contributions",
        className="my-2",
    )


def _map_group() -> Component:
    return html.Div(
        [
            _theme_dropdown(),
            _column_dropdown(),
            dcc.Graph(
                id="figure-map",
            ),
        ],
    )


app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            brand="Le grand Dashbat", className="mb-5", color="primary", dark=True
        ),
        dbc.Col(
            [
                html.H2("Carte des contributions par départements", className="my-2"),
                _map_group(),
                html.H2(
                    "Graphiques divers sur les données du grand débat", className="my-2"
                ),
                dcc.Graph(figure=dfig.get_figure_contributions_over_time()),
                dcc.Graph(figure=dfig.get_figure_contributions_per_type()),
                dcc.Graph(figure=dfig.get_figure_contributions_per_theme()),
                html.H2("Un premier graphique", className="my-2"),
                dcc.Graph(figure=dfig.get_figure_vancaces_lines_vs_remu()),
            ],
            width={"size": 10, "offset": 1},
        ),
    ]
)


@app.callback(
    Output("figure-map", "figure"),
    [
        Input("theme-dropdown", "value"),
        Input("display-column-dropdown", "value"),
    ],
)
def _select_dataset_for_map(theme: DatasetName, display_column: str) -> Component:
    return dfig.get_map_contributions_by_location(
        theme=theme, display_column=display_column
    )


def parse_args() -> argparse.ArgumentParser:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--port", type=int, default=8050)
    args_parser.add_argument("--host", type=ip_address, default=ip_address("127.0.0.1"))
    args_parser.add_argument("--debug", action="store_true", default=False)
    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app.run_server(debug=args.debug, host=str(args.host), port=args.port)
