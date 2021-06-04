import json
from urllib.request import urlopen

import plotly.express as px

import dashbat.data.data_layer as dal
from dashbat.data.data_types import DATASET_NAMES, DatasetName

with urlopen(
    "https://france-geojson.gregoiredavid.fr/repo/departements.geojson"
) as response:
    DEPTS = json.load(response)


def get_figure_vancaces_lines_vs_remu():
    data = [
        {"prenom": "Antoine", "vacances": 100},
        {"prenom": "Line", "vacances": 100},
    ]
    return px.bar(
        data,
        x="prenom",
        y="vacances",
        labels={
            "prenom": "Prénom",
            "vacances": "Durée moyenne des vacances (jours)",
        },
        title="Comparaison des nombre de jours de congés Line vs Rémi",
    )


def get_figure_contributions_per_theme():
    data = dal.get_num_contribution_per_theme()
    fig = px.bar(
        data,
        x="Thème",
        y="Nombre contributions",
        title="Nombre de contribution par thème",
    )
    tickvals = list(DATASET_NAMES.keys())
    ticktext = list(DATASET_NAMES.values())
    fig.update_xaxes(ticktext=ticktext, tickvals=tickvals)
    return fig


def get_figure_contributions_per_type():
    data = dal.get_num_contribution_per_type()
    fig = px.bar(
        data,
        x="Type de contributeur",
        y="Nombre contributions",
        text="Nombre contributions",
        title="Nombre de contributions par type de contributeur",
    )
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    return fig


def get_figure_contributions_over_time():
    data = dal.get_num_contribution_over_time()
    fig = px.line(
        data,
        x="Date",
        y="Nombre contributions",
        color="Thème",
        title="Nombre de contributions au cours du temps",
    )
    fig.update_layout(hovermode="x unified")
    return fig


def get_map_contributions_by_location(theme: DatasetName):
    display_column = "Nombre contributions"
    data = dal.get_map_per_theme(theme)

    fig = px.choropleth_mapbox(
        data,
        geojson=DEPTS,
        featureidkey="properties.code",
        locations="Departement",
        color=display_column,
        mapbox_style="carto-positron",
        zoom=4,
        center={"lat": 47, "lon": 2},
        opacity=0.5,
        title="Nombre de contributions par départements",
    )
    return fig
