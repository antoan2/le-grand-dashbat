import plotly.express as px

import dashbat.data.data_layer as dal
from dashbat.data.data_types import DATASET_NAMES


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
