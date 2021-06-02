import dash
import dash_core_components as dcc
import dash_html_components as html

from figures import (
    get_figure_contributions,
    get_figure_contributions_over_time,
    get_figure_contributions_per_type,
    get_map,
)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.H1(children="Le Grand Dashbat"),
        dcc.Graph(figure=get_figure_contributions()),
        dcc.Graph(figure=get_figure_contributions_over_time()),
        dcc.Graph(figure=get_figure_contributions_per_type()),
        dcc.Graph(figure=get_map(dataset_name="organisation")),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
