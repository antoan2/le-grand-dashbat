import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from app.bar_graph import BarGraph

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.H1(children="Le Grand Dashbat"),
        html.Div("Ceci est une div"),
        dcc.Checklist(
            options=[
                {"label": "option 1", "value": "1"},
                {"label": "option 2", "value": "2"},
                {"label": "option 3", "value": "3", "disabled": True},
            ],
            value=["2"],
        ),
        BarGraph(),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
