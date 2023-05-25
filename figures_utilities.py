import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd


Arap_outline = gpd.read_file('us-county-boundaries')



def get_Choropleth(df, geo_data, marker_opacity, fig=None):
    # print(df.index)
    # print(geo_data["FIPS"])
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
    #         mode="lines",
    #         lons = lons,
    #         lats = lats
    #     ))

    

    return fig


def get_figure(df, geo_data, geo_tracts_highlights):

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
    
    if len(geo_tracts_highlights) != 0:
        fig = get_Choropleth(df, geo_tracts_highlights, marker_opacity=1.0, fig=fig)
    

    return fig