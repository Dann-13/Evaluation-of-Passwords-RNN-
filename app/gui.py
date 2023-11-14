import tkinter as tk



class AppGUI:
    def __init__(self):
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
        self.resultado_texto.config(state=tk.NORMAL)  # Habilitar la edición del widget de texto
        self.resultado_texto.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.resultado_texto.insert(tk.END, f"La contraseña ingresada es segura: {contrasena_prueba}\n")
        self.resultado_texto.config(state=tk.DISABLED)  # Deshabilitar la edición del widget de texto
        
    def run(self):
        self.root.mainloop()
