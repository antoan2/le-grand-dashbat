import argparse
from ipaddress import ip_address

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_core_components.Markdown import Markdown
from dash_core_components.Slider import Slider
import dash_html_components as html

from dashbat.data.data_types import DATASET_NAMES, DatasetName


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)

app.layout = html.Div(
    children=[
        html.H1("Hello World !"),
        html.H2("Bonjour le monde !"),
        dcc.Checklist(
            options=[{"label": label, "value": label} for label in ["1", "2", "3"]]
        ),
        dcc.Slider(min=0, max=200, value=20, step=10),
        dcc.Input(type="text", placeholder="Voici un text input"),
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
