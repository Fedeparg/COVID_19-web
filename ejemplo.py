import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

operaciones = ["+","-","x","/"]

app.layout = html.Div(children=[
    html.H1(children='Intento de aplicación con Dash',
    style={'textAlign':'center'}),

    html.Div(children='Probando los dropdowns, valores de texto y callbacks.',
    style={'textAlign':'center'}),

    html.Div([
        html.H4("Pon un valor en las siguientes casillas y se aplicará la operación correspondiente:"),
    ]),

    html.Div([
        html.Div(["x: ", dcc.Input(id='x', value='0', type='number')]),
        html.Br(),

    ], 
    style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='operation',
            options=[{'label': i, 'value': i} for i in operaciones],
            value='+'
        ),
    ],
    style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Div(["y: ", dcc.Input(id='y', value='0', type='number')]),
        html.Br(),
    ],
    style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Div(id="result")
    ])
    
])

@app.callback(
    Output(component_id='result', component_property='children'),
    Input(component_id='x', component_property='value'),
    Input(component_id='y', component_property='value'),
    Input(component_id='operation', component_property='value')
)
def update_output_div(x, y, operation):
    if operation == "+":
        return 'Salida: {}'.format(int(x)+int(y))
    if operation == "x":
        return 'Salida: {}'.format(int(x)*int(y))
    if operation == "-":
        return 'Salida: {}'.format(int(x)-int(y))
    if operation == "/":
        if y == 0:
            return "La division entre 0 no está permitida"
        else:
            return 'Salida: {}'.format(int(x)/int(y))
    


if __name__ == '__main__':
    app.run_server(debug=True)