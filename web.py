import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# Esto es para que el desplegable funcione por ahora
operaciones = ["+","-","x","/"]

# Titulos cosas random
app.layout = html.Div(children=[
    html.H1(children='Modelos COVID-19',
    style={'textAlign':'center'}),

    html.Div(children='Desarrollado por la UM',
    style={'textAlign':'center'}),

    html.Div(children='''
        Selecciona un modelo.
    '''),
    html.Br(),

    # Seleccion del modelo 
    html.Div(['Modelos:', 
        dcc.Dropdown(
            id='operation',
            options=[{'label': i, 'value': i} for i in operaciones],
            value=''
        ),
    ],
    style={'width': '20%', 'display': 'inline-block'}),
    

    # Nos falta por incluir los datos de entrada para cada modelo. Entiendo que debe ser algo relativamente sencillo,
    # pero hasta que no lo concretemos (seleccion de variales), podemos dejarlo asi. Se haría de la misma forma que
    # en el script de ejemplo
])


if __name__ == '__main__':
    app.run_server(debug=True)