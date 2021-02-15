import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import components.header as header
import components.graph as graph

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div(
    children=[
        header.header,
        graph.get_graph("Date", "AveragePrice"),
        graph.get_graph("Date", "AveragePrice"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
