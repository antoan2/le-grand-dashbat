import plotly.express as px
import data_layer as dal


def get_figure_contributions():
    data = dal.get_num_contribution_per_theme()
    return px.bar(data, x="Thème", y="Nombre contribution")
