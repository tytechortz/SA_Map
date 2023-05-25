from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go

from figures_utilities import (
    get_figure
)

from utils import (
    get_svi_data,
    get_geo_data
)



app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")


template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}


df = get_svi_data()
geo_data = get_geo_data()

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
    tracts = {"FIPS":'8005080600'}

    # geo_tracts_highlights = dict()
    # print('sup')
    # print(geo_data.keys())

    geo_tracts_highlights = geo_data[geo_data['FIPS'].isin(['8005080600'])]
    # for k in geo_data.keys():
    #     if k != "geometry":
    #         geo_tracts_highlights[k] = geo_data[k]
    #     else:
    #         geo_tracts_highlights[k] = [
    #             geo_data[tract] 
    #             for tract in tracts
    #         ]
    print(geo_tracts_highlights)

    
    fig = get_figure(df, geo_data, geo_tracts_highlights)




    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)