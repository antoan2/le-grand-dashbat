import argparse
from ipaddress import ip_address

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.development.base_component import Component

from dashbat.data_types import DATASET_NAMES, DatasetName
from dashbat.figures import (
    get_figure_contributions,
    get_figure_contributions_over_time,
    get_figure_contributions_per_type,
    get_map,
)


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)


def _dataset_dropdown() -> Component:
    options = [{"value": id_, "label": name} for id_, name in DATASET_NAMES.items()]
    return dcc.Dropdown(id="dataset-dropdown", options=options, value="organisation")


def _column_dropdown() -> Component:
    options = [
        {"value": column, "label": column}
        for column in ["Nombre contributions", "Contributions 1 000 habitants"]
    ]

    return dcc.Dropdown(
        id="dataset-display-column", options=options, value="Nombre contributions"
    )


def _map_group() -> Component:
    return html.Div(
        [
            html.Div(
                [html.H3("Dataset"), _dataset_dropdown(), _column_dropdown()],
                className="col-3",
            ),
            html.Div(
                dcc.Graph(figure=get_map(dataset_name="organisation"), id="map-graph"),
                className="col-9",
            ),
        ],
        className="row",
    )


app.layout = html.Div(
    children=[
        html.Div(
            [
                html.H1(children="Le Grand Dashbat"),
                dcc.Graph(figure=get_figure_contributions()),
                dcc.Graph(figure=get_figure_contributions_over_time()),
                dcc.Graph(figure=get_figure_contributions_per_type()),
                _map_group(),
            ],
            className="container",
        )
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
    return get_map(dataset_name, display_column)


def parse_args() -> argparse.ArgumentParser:
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--port", type=int, default=8050)
    args_parser.add_argument("--host", type=ip_address, default="127.0.0.1")
    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app.run_server(debug=True, host="0.0.0.0", port="13524")
