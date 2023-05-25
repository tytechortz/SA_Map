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

tracts = geo_data["FIPS"].values

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
        dbc.Col([
            dcc.Dropdown(
                id="tracts",
                options=[
                    {"label": i, "value": i}
                    for i in tracts
                ],
                multi=True,
                style={"color": "black"},
                # value="SVI",
            ),
            dcc.Dropdown(id='graph-type')
        ], width=4)
    ])
])

@app.callback(
        Output("tracts", "value"),
        Input("sa-map", "clickData"),
        Input("sa-map", "selectedData"),
        Input("tracts", "value"),
        State("sa-map", "clickData")
)

def update_tract_dropdown(clickData, selectedData, tracts, clickData_state):

    if ctx.triggered[0]["value"] is None:
        return tracts
    
    # print(clickData)
    print(tracts)
    tract = ()

    changed_id = [p["prop_id"] for p in ctx.triggered][0]

    if clickData is not None and "customdata" in clickData["points"][0]:
        tract = clickData["points"][0]["customdata"]
        print(tract)
        if tract in tracts:
            tracts.remove(tract)
        elif len(tracts) < 5:
            tracts.append(tract)



    return tracts
    
    
    
    # changed_id = [p["prop_id"] for p in ctx.triggered][0]

    # if clickData is not None and ""

    # return tracts




@app.callback(
    Output("sa-map", "figure"),
    Input("map-category", "value"),
    # Input("graph-type", "value"),
    Input("tracts", "value")
)
def update_Choropleth(category, tracts):

    # changed_id = ctx.triggered[0][['prop_id'].split('.')[0]]
    # print(changed_id)
    
    geo_tracts_highlights = ()
    
    if tracts != None:
        geo_tracts_highlights = geo_data[geo_data['FIPS'].isin(tracts)]
    
        # print(geo_tracts_highlights)

    
    fig = get_figure(df, geo_data, geo_tracts_highlights)




    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)