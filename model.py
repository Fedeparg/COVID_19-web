from abc import ABC, abstractmethod


class model(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def predictors(self):
        '''
        Devuelve la lista de strings con los nombres de los predictores,
        el tipo, el rango de valores que puede tomar y una explicación
        sobre los mismos.
        '''
        pass

    @abstractmethod
    def predict(self):
        '''
        Realiza una predicción con el modelo seleccionado y los
        datos proporcionados por el usuario.
        '''
        pass

    @abstractmethod
    def outcome(self):
        '''
        El tipo de salida que genera (si es una distribución de probabilidad,
        un valor de clases, …)
        '''
        pass

    @abstractmethod
    def dataset(self):
        '''
        Un string con el dataset tal y como se puede acceder a él desde
        prodia.inf.um.es
        '''
        pass

    @abstractmethod
    def markdown(self):
        '''
        Un string con el markdown que lo creó, accesible también desde
        prodia.inf.um.es
        '''
        pass

    @abstractmethod
    def model_type(self):
        '''
        Una lista de pares atributo-valor con el algoritmo y los
        correspondientes valores para los hiperparámetros.
        '''
        pass
