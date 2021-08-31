import pandas as pd
import sys
import numpy as np
import pickle

from sklearn import preprocessing
from tensorflow.keras.models import load_model


def parse_algorithm(algorithm, estratificacion, selene):
    if algorithm == 'Random Forest':
        return random_forest()
    elif algorithm == 'CNN':
        return cnn()
    elif algorithm == 'CNN + MLP':
        return cnn_mlp()


def process_selene(selene, estratificacion=None, ventana=15):

    final = pd.DataFrame()

    test = selene.copy()
    columns = test.columns
    test = test.reset_index()

    # Cogemos los dias de ventana
    test.reset_index(inplace=True, drop=True)

    # Rellenamos hasta llegar al tamaño de ventana
    if test.shape[0] < 15:
        test2 = test.append(test.iloc[[-1]*(15-test.shape[0])])
    # Rellenamos los nulos hacia delante. Esto se usa para conservar el ID del usuario
    # en las filas generadas
    test2 = test2.ffill()
    test2.reset_index(inplace=True, drop=True)

    # Si se ha pasado el dataset de estratificación,
    # se realiza la misma operacion que para SELENE
    if estratificacion is not None:
        estr = estratificacion.copy()
        estr.reset_index(inplace=True)
        estr = estr.rename(columns={'ID_PACIENTE': 'ID_PACIENTE_DROP'})

        # Repetimos el tamaño de ventana en filas
        test5 = estr.copy()
        if test5.shape[0] < 15:
            test5 = test5.append(test5.iloc[[-1]*(15-test5.shape[0])])
            test5.reset_index(inplace=True)
            test5.drop(columns=['index'], inplace=True)

        # Concatenamos los dataframes y nos cargamos la columna ID que sobra
        test2 = pd.concat((test2.copy(), test5.copy()), axis=1)
        test2 = test2.drop(columns=['ID_PACIENTE_DROP'])

    if final.empty:
        final = test2.copy()
    else:
        final = final.append(test2.copy(), ignore_index=True)

    # NUMPY
    x = None
    if estratificacion is None:

        test = final.copy()
        test = test.drop(columns=['ID_PACIENTE', 'FECHA_TOMA'])
        test2 = test.to_numpy()

        test3 = test2

        if x is None:
            x = test3
        else:
            x = np.append(x, test3, axis=0)

        # el escalado se hace aquí porque no se puede escalar un array 3d
        scaler_selene = preprocessing.StandardScaler()
        x = scaler_selene.fit_transform(x)

        x = x.reshape(1, test2.shape[0], test2.shape[1], 1)

    else:
        test = final.copy()
        test = test.drop(columns=['ID_PACIENTE', 'FECHA_TOMA'])
        test2 = test.to_numpy()
        test2 = test2.flatten()
        test2 = test2.reshape(1, test2.shape[0])

        if x is None:
            x = test2
        else:
            x = np.concatenate((x, test2))
    return x


def random_forest():
    model = pickle.load(open('./rf.pickle', 'rb'))
    selene = pd.read_csv(
        './project/app_uploaded_files/selene_test', index_col = [0, 1])
    estratificacion = pd.read_csv(
        './project/app_uploaded_files/estratificacion_test', index_col=0)
    x = process_selene(selene, estratificacion=estratificacion, ventana=15)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    result = model.predict(x_scaled)[0]
    return round(result)


def cnn():
    model = load_model('./cnn.h5')
    selene = pd.read_csv(
        './project/app_uploaded_files/selene_test', index_col = [0, 1])
    estratificacion = pd.read_csv(
        './project/app_uploaded_files/estratificacion_test', index_col=0)
    x = process_selene(selene, estratificacion=estratificacion, ventana=15)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    x_scaled = x_scaled.reshape(x_scaled.shape[0], x_scaled.shape[1], 1)
    result = model.predict(x=x_scaled)[0][0]
    return round(result)


def cnn_mlp():
    model = load_model('./cnn_mlp.h5')
    selene = pd.read_csv(
        './project/app_uploaded_files/selene_test', index_col=0)
    selene_procesado = process_selene(selene, ventana=15)

    estratificacion = pd.read_csv(
        './project/app_uploaded_files/estratificacion_test', index_col=0)
    selene.drop(columns=['FECHA_TOMA'], inplace=True)

    estratificacion = estratificacion.values

    scaler_estratificacion = preprocessing.StandardScaler()
    estratificacion_scaled = scaler_estratificacion.fit_transform(
        estratificacion)

    result = model.predict(x=[estratificacion_scaled, selene_procesado])[0][0]
    return round(result)
