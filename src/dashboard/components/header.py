import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import components.indicator as indicator

header = (html.Div(
    children=[
        html.Img(src="/assets/logo.svg",
                 alt="My Happy SVG", id="logo"),
        html.H1(children="WizCrunch",
                className="header-title"),
        html.Div(children=[
            indicator.show_status("Tobii", True),
            indicator.show_status("Empirica E4", True),
            indicator.show_status("openPose", True),
        ], className="indicator-panel")
    ],
    className="header",
))
