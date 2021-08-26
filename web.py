import base64
import os
from urllib.parse import quote as urlquote

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, send_from_directory


UPLOAD_DIRECTORY = "./tmp/"

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
                    id='operation',
                    options=[{'label': i, 'value': i} for i in operaciones],
                    value=''
                ),
                html.Br(),


            ],
            style={'width': '50%', 'display': 'inline-block'}),
        html.Br(),


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
        html.H2("File List"),
        html.Ul(id="file-list"),


    ], style={'columnCount': 3}),
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
    app.run_server(debug=True, host = '0.0.0.0')
