### scr/train.py example
import os
import pickle

## Cambiamos el path en el que estamos trabajando al path donde está este archivo '.py'
os.chdir(os.path.dirname(__file__))

## Cargamos el modelo
filename = 'finished_model.pkl'
with open(filename, 'rb') as archivo_entrada:
    modelo_mejor = pickle.load(archivo_entrada)

## Miramos si cargamos bien el modelo, si nos da la descripción del modelo, lo hemos cargado bien y podremos utilizarlo en este script
print(modelo_mejor)

'''

Ejemplo aplicación:

Digamos que tenemos un modelo de linear regression que fue entrenado con tres variables, edad, altura y peso, y con el podemos predecir el
estado físico:

* Primero guardamos las features (edad, altura, peso) a partir de las cuales queremos predecir el target (estado físico) en variables:

edad = input()
altura = input()
peso = input()

--- Nota: Si hubiesemos escalado las variables para entrenar el modelo que cargamos, tendríamos que escalar también dichas variables 
para poder predecir con nuestro modelo.

array_de_features = np.array([edad, altura, peso])
prediccion = modelo_mejor.predict(array_de_features)
print(prediccion) #Obtendremos la predicción a partir de los valores de edad, altura y peso que le dimos como input

'''