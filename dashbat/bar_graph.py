import plotly.express as px
from dash_core_components import Graph

DATA = [
    {"prenom": "Antoine", "vacances": 100},
    {"prenom": "Rémi", "vacances": 0},
    {"prenom": "Line", "vacances": 100},
    {"prenom": "Jordan", "vacances": 365},
]


def BarGraph():
    fig = px.bar(
        DATA,
        x="prenom",
        y="vacances",
        labels={
            "prenom": "Prénom",
            "vacances": "Durée moyenne des vacances (jours)",
        },
    )

    return Graph(figure=fig)
