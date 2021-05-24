import data_layer as dal
import plotly.express as px


def get_figure_contributions():
    data = dal.get_num_contribution_per_theme()
    return px.bar(data, x="Thème", y="Nombre contribution")


def get_figure_contributions_over_time():
    data = dal.get_num_contribution_over_time()
    return px.line(data, x="Date", y="Nombre contributions", color="Catégorie")


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
