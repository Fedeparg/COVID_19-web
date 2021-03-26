import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Esto es para que el desplegable funcione por ahora
operaciones = ["+", "-", "x", "/"]

# Titulos cosas random
app.layout = html.Div(children=[
    html.H1(children='Modelos COVID-19',
            style={'textAlign': 'center'}),

    html.Div(children='Desarrollado por la Universidad de Murcia',
             style={'textAlign': 'center'}),

    html.Br(),

    html.Div([

        # Columna Izquierda
        html.Div(

            [
                # Seleccion de modelo
                'Selecciona un modelo:',
                dcc.Dropdown(
                    id='operation',
                    options=[{'label': i, 'value': i} for i in operaciones],
                    value=''
                ),
                html.Br(),

                # Ingreso
                'Ingreso:', dcc.RadioItems(
                    id='ingreso',
                    options=[{'label': i, 'value': i}
                             for i in ['Si', 'No']],
                    value='No',
                    labelStyle={'display': 'inline-block'}
                ),
                html.Br(),

                # NPC (Numero Patologias Cronicas)
                'NPC (Numero Patologias Cronicas):', dcc.Input(
                    id='npc',
                    value='0',
                    type='number'
                ),
                html.Br(),
                html.Br(),

                # Estrato
                'Estrato:', dcc.Input(
                    id='estrato',
                    value='0',
                    type='number'
                ),

                html.Br(),
                html.Br(),

                # HTA
                'HTA', dcc.RadioItems(
                    id='hta',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # DEP
                'DEP', dcc.RadioItems(
                    id='dep',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # VIH
                'VIH', dcc.RadioItems(
                    id='vih',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # IRC
                'IRC', dcc.RadioItems(
                    id='irc',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # OST
                'OST', dcc.RadioItems(
                    id='ost',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # Artritis
                'Artritis', dcc.RadioItems(
                    id='Artritis',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # DC
                'DC', dcc.RadioItems(
                    id='dc',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
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

                # Edad
                'Edad', dcc.Input(id='edad', value='', type='number'),

                html.Br(),
                html.Br(),

                # NSIST
                'NSIST:', dcc.Input(
                    id='nsist',
                    value='0',
                    type='number'
                ),

                html.Br(),
                html.Br(),

                # DM
                'DM', dcc.RadioItems(
                    id='dm',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # IC
                'IC', dcc.RadioItems(
                    id='ic',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # EPOC
                'EPOC', dcc.RadioItems(
                    id='epoc',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # CI
                'CI', dcc.RadioItems(
                    id='ci',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # ACV
                'ACV', dcc.RadioItems(
                    id='acv',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # CIR
                'CIR', dcc.RadioItems(
                    id='cir',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # Artrosis
                'Artrosis', dcc.RadioItems(
                    id='artrosis',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),

                html.Br(),

                # DEM
                'DEM', dcc.RadioItems(
                    id='dem',
                    options=[{'label': i, 'value': i}
                             for i in ['Verdadero', 'Falso']],
                    value='Falso',
                    labelStyle={'display': 'inline-block'}
                ),


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
    app.run_server(debug=False, host = '0.0.0.0', port = 5050)
