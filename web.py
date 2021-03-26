import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# Esto es para que el desplegable funcione por ahora
operaciones = ["+", "-", "x", "/"]

# Titulos cosas random
app.layout = html.Div(children=[
    html.H1(children='Modelos COVID-19',
            style={'textAlign': 'center'}),

    html.Div(children='Desarrollado por la Universidad de Murcia',
             style={'textAlign': 'center'}),

    html.Div([

        # Columna Izquierda
        html.Div(
            # Seleccion de modelo
            [
                'Selecciona un modelo:',
                dcc.Dropdown(
                    id='operation',
                    options=[{'label': i, 'value': i} for i in operaciones],
                    value=''
                ),

            ],
            style={'width': '50%', 'display': 'inline-block', 'marginLeft': '10%', 'align': 'center'}),

        html.Div(html.Br(), style={'width': '20%', 'display': 'inline-block'}),

        # Columna derecha
        html.Div(
            # Sexo
            [
                'Género:', dcc.RadioItems(
                    id='sexo',
                    options=[{'label': i, 'value': i}
                             for i in ['Hombre', 'Mujer']],
                    value='Hombre',
                    labelStyle={'display': 'inline-block'}
                ),
                html.Br(),

                'Edad', dcc.Input(id='edad', value='', type='number'),



            ],
            style={'width': '50%', 'display': 'inline-block'}),
        html.Br(),

        # Edad



    ], style={'columnCount': 3}),
    # Nos falta por incluir los datos de entrada para cada modelo. Entiendo que debe ser algo relativamente sencillo,
    # pero hasta que no lo concretemos (seleccion de variales), podemos dejarlo asi. Se haría de la misma forma que
    # en el script de ejemplo
],)


if __name__ == '__main__':
    app.run_server(debug=True)
