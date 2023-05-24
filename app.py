from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go

from figures_utilities import (
    get_figure
)



app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")


template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}


def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }



app.layout = dbc.Container([
    header,
    dbc.Row(dcc.Graph(id='sa-map', figure=blank_fig(500))),
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id="map-category",
                options=[
                    {"label": i, "value": i}
                    for i in ["SVI", "Facilities"]
                ],
                value="SVI",
                inline=True
            ),
        ], width=2),
    ])
])


@app.callback(
    Output("sa-map", "figure"),
    Input("map-category", "value"),
    # Input("graph-type", "value"),
    # Input("tracts", "value")
)
def update_Choropleth(category):
    
    fig = get_figure()




    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)