import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd


Arap_outline = gpd.read_file('us-county-boundaries')



def get_Choropleth(df, geo_data, marker_opacity, fig=None):
    print(df.index)
    print(geo_data["FIPS"])
    if fig is None:
        fig = go.Figure()

    fig.add_trace(
        go.Choroplethmapbox(
            geojson=eval(geo_data['geometry'].to_json()),
            locations=df.index,
            z=df['E_TOTPOP'],
            marker_opacity = marker_opacity
        )
    )

    return fig

def get_map(df):

    fig = go.Figure()
    # fig.add_trace(
    #     go.Scattermapbox(
    #         mode="lines",
    #         lat = df
    #     )
    # )
    # fig.update_layout(
    #     mapbox={

    #     }
    # )
    
    # fig = go.Figure(go.Scattermapbox(
    #         mode="markers",
    #         lon = [-73.605], 
    #         lat = [45.51],
    #     ))

    

    return fig


def get_figure(df, geo_data):

    # fig = go.Figure(
    #     go.Scattermapbox(
    
    #     )
    # )
    fig = get_Choropleth(df, geo_data, marker_opacity=0.4)
    # things = get_map(df)
    # fig.add_trace(things.data[0])
    # layer = [
    #         {
    #             "source": geo_data["geometry"].__geo_interface__,
    #             "type": "line",
    #             "color": "red"
    #         }
    #     ]
    
    fig.update_layout(mapbox_style="carto-positron", 
                            mapbox_zoom=10.4,
                            # mapbox_layers=layer,
                            mapbox_center={"lat": 39.65, "lon": -104.8},
                            margin={"r":0,"t":0,"l":0,"b":0},
                            uirevision='constant')
    

    return fig