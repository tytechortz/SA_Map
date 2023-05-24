from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go



app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

app.layout = dbc.Container([
    header,
])





if __name__ == "__main__":
    app.run_server(debug=True, port=8080)