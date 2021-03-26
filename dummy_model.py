from model import model
import fileinput
import re

def main():
    a = dummy_model('./dummy.md')
    print(a.predictors())
    print(a.dataset())
    print(a.markdown())

class dummy_model(model):

    def __init__(self, markdown):
        self.md = markdown

    def predictors(self):
        return "Predictores"

    def predict(self):
        '''
        Realiza una predicción con el modelo seleccionado y los
        datos proporcionados por el usuario.
        '''
        pass

    def outcome(self):
        '''
        El tipo de salida que genera (si es una distribución de probabilidad,
        un valor de clases, …)
        '''
        pass

    def dataset(self):
        '''
        Un string con el dataset tal y como se puede acceder a él desde
        prodia.inf.um.es
        '''
        with open(self.md, "r+") as md:
            for line in md:
                if "## Dataset" in line:
                    x = re.search("([a-zA-Z0-9\/]+)", md.readline())
        return x.group(1)
        

    def markdown(self):
        '''
        Un string con el markdown que lo creó, accesible también desde
        prodia.inf.um.es
        '''
        return self.md

    def model_type(self):
        '''
        Una lista de pares atributo-valor con el algoritmo y los
        correspondientes valores para los hiperparámetros.
        '''
        pass

if __name__ == "__main__":
    main()