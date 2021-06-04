import argparse
from ipaddress import ip_address

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.development.base_component import Component

from dashbat.data.data_types import DATASET_NAMES, DatasetName
import dashbat.figures as dfig


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)


def _dataset_dropdown() -> Component:
    options = [{"value": id_, "label": name} for id_, name in DATASET_NAMES.items()]
    return dcc.Dropdown(
        id="dataset-dropdown", options=options, value="organisation", className="my-2"
    )


def _column_dropdown() -> Component:
    options = [
        {"value": column, "label": column}
        for column in ["Nombre contributions", "Contributions 1 000 habitants"]
    ]

    return dcc.Dropdown(
        id="dataset-display-column",
        options=options,
        value="Nombre contributions",
        className="my-2",
    )


def _map_group() -> Component:
    return html.Div(
        [
            dcc.Markdown(
                """
                        ## Contribution par département
                        Affichons le nombre de contributions par département.
                        """
            ),
            _dataset_dropdown(),
            _column_dropdown(),
            dcc.Graph(
                figure=dfig.get_map(
                    dataset_name="organisation",
                    display_column="Nombre contributions",
                ),
                id="map-graph",
                className="my-4",
            ),
        ],
    )


app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            brand="Le grand Dashbat", className="mb-6", color="primary", dark=True
        ),
        dbc.Col(
            [
                _map_group(),
                dcc.Graph(figure=dfig.get_figure_contributions_over_time()),
                dcc.Graph(figure=dfig.get_figure_contributions_per_type()),
                dcc.Graph(figure=dfig.get_figure_contributions_per_theme()),
                dcc.Graph(figure=dfig.get_figure_vancaces_lines_vs_remu()),
            ],
            width={"size": 8, "offset": 2},
        ),
    ]
)


@app.callback(
    Output("map-graph", "figure"),
    [
        Input("dataset-dropdown", "value"),
        Input("dataset-display-column", "value"),
    ],
    prevent_initial_call="True",
)
def _select_dataset_for_map(dataset_name: DatasetName, display_column) -> Component:
    return dfig.get_map(dataset_name, display_column)


def parse_args() -> argparse.ArgumentParser:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--port", type=int, default=8050)
    args_parser.add_argument("--host", type=ip_address, default=ip_address("127.0.0.1"))
    args_parser.add_argument("--debug", action="store_true", default=False)
    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app.run_server(debug=args.debug, host=str(args.host), port=args.port)
