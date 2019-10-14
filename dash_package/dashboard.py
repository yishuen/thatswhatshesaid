import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_package import app
from dash_package.functions import *

x = [1, 2, 3, 4, 5]

app.layout = html.Div(children=[
    html.H1('welcome!', style={'color': 'red', 'font-family': 'verdana', 'textAlign': 'center'}),
    dcc.Link('to the classifier!!', href='/model', style={'color': 'red', 'font-family': 'verdana', 'textAlign': 'center'}),

])
