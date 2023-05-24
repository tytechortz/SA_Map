import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd


Arap_outline = gpd.read_file('us-county-boundaries')



def get_Choropleth(df, geo_data, fig=None):
    
    if fig is None:
        fig = go.Figure()

    fig.add_trace(
        go.Choroplethmapbox(
            geojson = eval(geo_data['geometry'].to_json()),
            locations = df.index,
            z = df['E_TOTPOP']
        )
    )

    return fig


def get_figure(df, geo_data):

    # fig = go.Figure(
    #     go.Scattermapbox(
    
    #     )
    # )
    fig = get_Choropleth(df, geo_data)
    # layer = [
    #         {
    #             "source": Arap_outline["geometry"].__geo_interface__,
    #             "type": "line",
    #             "color": "black"
    #         }
    #     ]
    
    fig.update_layout(mapbox_style="carto-positron", 
                            mapbox_zoom=10.4,
                            # mapbox_layers=layer,
                            mapbox_center={"lat": 39.65, "lon": -104.8},
                            margin={"r":0,"t":0,"l":0,"b":0},
                            uirevision='constant')
    

    return fig