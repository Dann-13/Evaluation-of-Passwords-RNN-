import tkinter as tk
from tkinter import messagebox

def evaluar_contrasena():
    contrasena_prueba = entrada_contraseña.get()
    messagebox.showinfo("Contraseña Evaluada", f"Contraseña ingresada: {contrasena_prueba}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Evaluador de Contraseñas")

# Etiqueta y entrada para ingresar la contraseña
etiqueta_contraseña = tk.Label(ventana, text="Ingresa la contraseña:")
etiqueta_contraseña.pack(pady=10)

entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.pack(pady=10)

# Botón para evaluar la contraseña
boton_evaluar = tk.Button(ventana, text="Evaluar Contraseña", command=evaluar_contrasena)
boton_evaluar.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
