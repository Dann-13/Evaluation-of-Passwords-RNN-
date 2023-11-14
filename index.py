import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
from tensorflow.keras.models import load_model



from IPython.display import display
# Carga el archivo CSV en un DataFrame
# Especificamos las columnas que necesitamos en este caso para el dataset son las columnas 0 y 1, a su vez solo cargaremos 2000
#registros del dataset
df = pd.read_csv('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/data.csv', usecols=[0, 1], nrows=2000)
# Visualizamos de manera intuitiva el dataset
display(df)


# Tokenización de las contraseñas
#iniciamos con tokenizar las contraseñas para que las dibida en caracteres en lugar de palabras
tokenizer = Tokenizer(char_level=True)
#Ajustamos el Tokenizer a las contraseñas de la columna 'password' del DataFrame. Durante este proceso,
# el tokenizer aprende el vocabulario de caracteres presentes en todas las contraseñas.
tokenizer.fit_on_texts(df['password'])
# Convierte las contraseñas en secuencias de números enteros. Cada número entero representa un carácter
# en el vocabulario aprendido por el tokenizer.
X_entrenamiento = tokenizer.texts_to_sequences(df['password'])
# Para que todas las secuencias tengan la misma longitud
X_entrenamiento = pad_sequences(X_entrenamiento)

# almacenamos las etiquetas que representan la fuerza de las contraseñas , donde 0 es "débil", 1 es "segura" y 2 es "bastante segura"
etiquetas = np.array(df['strength'])

# Creación del modelo RNN para evaluar contraseñas
model = tf.keras.Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=X_entrenamiento.shape[1]),
    #Es una capa de memoria a largo plazo que ayuda al modelo a aprender patrones y relaciones a lo largo de las secuencias de contraseñas.
    LSTM(128),
    Dense(3, activation='softmax')  # Capa de salida con activación softmax para clasificación de tres clases
])
#compilamos el modelo
#utilizamos sparse_categorical_crossentropy que es apropiada problemas de clasificacion en donde hay varias clases, en nuestro caso son 3
#3 categorias debil segura y bastante segura, usamos adam para optimizar el proceso de aprendiaje y por ultimo usamos la metrica
#accurracy para evaluar el desempeño del modelo en las etapas
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#nos aseguramos que las etiquetas sean del tipo de dato entero para que el modelo pueda funcionar correctamente
etiquetas = etiquetas.astype(int)
# Finalmente entrenamos el modelo, en donde usa las secuencias de contraseñas X_entrenamiento y las etiquetas de fuerza
# seran 10 epocas con un lote, esto hara que se actualice despues de procesar cada contraseña del dataser, para que finalmente
# el modelo aprenda a categorizar contraseñas en 3 categorias
model.fit(X_entrenamiento, etiquetas, epochs=10, batch_size=1)

# Guardamos el modelo entrenado para usarlo despues
model.save('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/modelo_RNN.h5')
