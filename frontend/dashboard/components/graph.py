import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)


def get_graph(x, y):
    return (
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        figure={
                            "data": [
                                {
                                    "x": data[x],
                                    "y": data[y],
                                    "type": "lines",
                                },
                            ],
                            "layout": {"title": "Average Price of Avocados"},
                        },
                    )
                )
            ]
        )
    )
