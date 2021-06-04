import argparse
from ipaddress import ip_address

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_core_components.Markdown import Markdown
from dash_core_components.Slider import Slider
import dash_html_components as html

from dashbat.data.data_types import DATASET_NAMES, DatasetName
import dashbat.figures as dfig


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)
app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            brand="Le grand Dashbat", className="mb-5", color="primary", dark=True
        ),
        dbc.Col(
            [
                html.H2("Un premier graphique"),
                dcc.Graph(figure=dfig.get_figure_vancaces_lines_vs_remu()),
            ],
            width={"size": 10, "offset": 1},
        ),
    ]
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
