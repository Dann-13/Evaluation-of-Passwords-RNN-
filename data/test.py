import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

# Cargar el modelo entrenado
modelo_cargado = load_model('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/modelo_RNN.h5')

# Cargar el tokenizer desde el archivo JSON
tokenizer_json = open('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/tokenizer.json', 'r').read()
tokenizer = tokenizer_from_json(tokenizer_json)

longitud_maxima = 35

# Contraseña de prueba
contrasena_prueba = "Sebas"

# Tokenización de la contraseña de prueba
contrasena_prueba_seq = tokenizer.texts_to_sequences([contrasena_prueba])
contrasena_prueba_seq = pad_sequences(contrasena_prueba_seq, maxlen=longitud_maxima)

# Realizar la predicción utilizando el modelo cargado
prediccion = modelo_cargado.predict(contrasena_prueba_seq)

# Obtener la clasificación numérica
clasificacion_numerica = np.argmax(prediccion, axis=1)

# Obtener la probabilidad de cada clase
probabilidades = prediccion[0]

# Imprimir la clasificación numérica y las probabilidades
print(f"Clasificación numérica de la contraseña: {clasificacion_numerica[0]}")
print(f"Probabilidades de cada clase (Débil, Segura, Bastante Segura): {probabilidades}")
