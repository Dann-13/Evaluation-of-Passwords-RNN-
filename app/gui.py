import tkinter as tk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

class AppGUI:
    def __init__(self):
         # Cargar el modelo entrenado
        self.modelo_cargado = load_model('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/modelo_RNN.h5')

        # Cargar el tokenizer desde el archivo JSON
        tokenizer_json = open('/home/dan-dev/Documents/Proyectos_Personales/Proyects_Python/ProyectoIAContraseñas/data/tokenizer.json', 'r').read()
        self.tokenizer = tokenizer_from_json(tokenizer_json)
        
        self.root = tk.Tk()
        self.root.title("Mi Aplicación")
        self.root.geometry("900x500")
        # Aquí puedes agregar widgets y configuraciones de la interfaz gráfica
        
        # Crear un marco principal para dividir la ventana
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Lado izquierdo (azul)
        left_frame = tk.Frame(frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #contenedor lado izquierdo
        left_cotainer = tk.Frame(left_frame)
        left_cotainer.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Etiqueta y entrada para ingresar la contraseña
        self.etiqueta_contraseña = tk.Label(left_cotainer, text="Texto descriptivo")
        self.etiqueta_contraseña.grid(row=0, column=0, pady=10)

        # Lado derecho (rojo)
        right_frame = tk.Frame(frame, bg="red")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Contenedor para elementos en el lado derecho
        right_container = tk.Frame(right_frame, bg="red")
        right_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Etiqueta y entrada para ingresar la contraseña
        self.etiqueta_contraseña = tk.Label(right_container, text="Ingresa la contraseña:")
        self.etiqueta_contraseña.grid(row=0, column=0, pady=10)

        self.entrada_contraseña = tk.Entry(right_container, show="*")
        self.entrada_contraseña.grid(row=1, column=0, pady=10)

        # Botón para evaluar la contraseña
        self.boton_evaluar = tk.Button(right_container, text="Evaluar Contraseña", command=self.evaluar_contrasena)
        self.boton_evaluar.grid(row=2, column=0, pady=10)

        # Widget de texto para mostrar el resultado
        self.resultado_texto = tk.Text(right_container, height=4, width=50)
        self.resultado_texto.grid(row=3, column=0, pady=10)
        self.resultado_texto.config(state=tk.DISABLED) 
    def evaluar_contrasena(self):
        contrasena_prueba = self.entrada_contraseña.get()
        # Tokenización de la contraseña de prueba
        contrasena_prueba_seq = self.tokenizer.texts_to_sequences([contrasena_prueba])
        contrasena_prueba_seq = pad_sequences(contrasena_prueba_seq, maxlen=35)  # Usa la longitud máxima que determinaste

        # Realizar la predicción utilizando el modelo cargado
        prediccion = self.modelo_cargado.predict(contrasena_prueba_seq)

        # Obtener la clasificación numérica
        clasificacion_numerica = np.argmax(prediccion, axis=1)

        # Obtener la probabilidad de cada clase
        probabilidades = prediccion[0]
        # Mostrar el resultado en el widget de texto
        resultado = f"Clasificación numérica de la contraseña: {clasificacion_numerica[0]}\nProbabilidades de cada clase (Débil, Segura, Bastante Segura): {probabilidades}\n"
        self.resultado_texto.config(state=tk.NORMAL)  # Habilitar la edición del widget de texto
        self.resultado_texto.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.resultado_texto.insert(tk.END, resultado)
        self.resultado_texto.config(state=tk.DISABLED)  # Deshabilitar la edición del widget de texto

    def run(self):
        self.root.mainloop()