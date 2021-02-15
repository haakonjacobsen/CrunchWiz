import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def show_status(devicename, receiving):
    if receiving:
        color = "#A4F456"
    else:
        color = "#F45656"
    return (html.Div(
        children=[
            html.Div(style={"height": "35px",
                            "width": "35px",
                            "backgroundColor": color,
                            "borderRadius": "25px"
                            }, className="device-status"),
            html.H1(children=devicename,
                    className="device-title"),
        ],
        className="device-indicator",
    ))
