import base64
import os
from urllib.parse import quote as urlquote

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import Flask, send_from_directory


from data_processing import parse_algorithm, cnn_mlp


UPLOAD_DIRECTORY = "./project/app_uploaded_files/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

server = Flask(__name__)
app = Dash(name='web', server=server)

# Esto es para que el desplegable funcione por ahora
operaciones = ["Random Forest", "CNN", "CNN + MLP"]


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


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
                    id='model',
                    options=[{'label': i, 'value': i} for i in operaciones],

                    value=''
                ),
                html.Br(),


            ],
            style={'width': '50%', 'display': 'inline-block'}),

        html.Br(),
        html.Div([
            html.H2("File List"),
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    ["Drag and drop or click to select a file to upload."]
                ),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=True,
            ),
            html.Br(),
            html.Ul(id="file-list"),
        ],
            style={'width': '50%', 'display': 'inline-block'}),
    ], style={'columnCount': 2}),
    html.Br(),
    html.Div([
        html.Button(children='Procesar', id='button', n_clicks=0)
    ]),
    html.Div(id='output-container',
             children='Presiona el botón tras haber seleccionado un algoritmo y haya algún par de ficheros subidos.')
],)


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output('output-container', 'children'),
    Input('button', 'n_clicks'),
    State('model', 'value'))
def update_output(n_clicks, value):
    try:
        estr = open('./project/app_uploaded_files/estratificacion_test')
        selene = open('./project/app_uploaded_files/selene_test')
    except IOError:
        print('File not accesible')

    finally:
        estr.close()
        selene.close()

    if value is not "":
        resultado = parse_algorithm(value, estr, selene)
        return 'Con el modelo seleccionado "{}" y el fichero incluido, se devuelve como resultado "{}". 0 representa la supervivencia del paciente y 1 su defunción'.format(
            value,
            resultado
        )
    else:
        return 'Seleccione un modelo.'


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("Sin ficheros subidos.")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
