import json
from urllib.request import urlopen

import plotly.express as px

import data_layer as dal


def get_figure_contributions():
    data = dal.get_num_contribution_per_theme()
    return px.bar(data, x="Thème", y="Nombre contribution")


def get_figure_contributions_over_time():
    data = dal.get_num_contribution_over_time()
    fig = px.line(data, x="Date", y="Nombre contributions", color="Catégorie")
    fig.update_layout(hovermode="x unified")
    return fig


def get_figure_contributions_per_type():
    data = dal.get_num_contribution_per_type()
    fig = px.bar(
        data,
        x="Type de contributeur",
        y="Nombre contributions",
        text="Nombre contributions",
    )
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    return fig


def get_map(dataset_name: str):
    data = dal.get_map_per_theme(dataset_name)

    with urlopen(
        "https://france-geojson.gregoiredavid.fr/repo/departements.geojson"
    ) as response:
        depts = json.load(response)

    fig = px.choropleth_mapbox(
        data,
        geojson=depts,
        featureidkey="properties.code",
        locations="Departement",
        color="Nombre contributions",
        mapbox_style="carto-positron",
        zoom=4,
        center={"lat": 46, "lon": 2},
        opacity=0.5,
    )
    return fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
