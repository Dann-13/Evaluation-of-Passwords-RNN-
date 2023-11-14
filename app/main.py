import tkinter as tk
from tkinter import messagebox

def evaluar_contrasena():
    contrasena_prueba = entrada_contraseña.get()
    resultado_texto.config(state=tk.NORMAL)  # Habilitar la edición del widget de texto
    resultado_texto.delete(1.0, tk.END)  # Limpiar el contenido anterior
    resultado_texto.insert(tk.END, f"La contraseña ingresada es segura: {contrasena_prueba}\n")
    resultado_texto.config(state=tk.DISABLED)  # Deshabilitar la edición del widget de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Evaluador de Contraseñas")
ventana.geometry("800x500")

# Crear el contenedor de la izquierda
frame_izquierdo = tk.Frame(ventana)
frame_izquierdo.pack(side=tk.LEFT, padx=10)

# Crear el contenedor de la derecha
frame_derecho = tk.Frame(ventana)
frame_derecho.pack(side=tk.RIGHT, padx=10)

# Etiqueta y entrada para ingresar la contraseña
etiqueta_contraseña = tk.Label(frame_derecho, text="Ingresa la contraseña:")
etiqueta_contraseña.pack(pady=10)

entrada_contraseña = tk.Entry(frame_derecho, show="*")
entrada_contraseña.pack(pady=10)

# Botón para evaluar la contraseña
boton_evaluar = tk.Button(frame_derecho, text="Evaluar Contraseña", command=evaluar_contrasena)
boton_evaluar.pack(pady=10)

# Widget de texto para mostrar el resultado
resultado_texto = tk.Text(frame_derecho, height=4, width=50)
resultado_texto.pack(pady=10)
resultado_texto.config(state=tk.DISABLED)  # Inicialmente, deshabilitar la edición del widget de texto

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
