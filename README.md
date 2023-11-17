# Contraseña Segura Classifier

Este proyecto implementa un clasificador de contraseñas utilizando una Red Neuronal Recurrente (RNN) entrenada en un conjunto de datos previamente clasificado. El modelo clasifica las contraseñas en tres categorías: débil (0), segura (1) y bastante segura (2). Además, proporciona la probabilidad asociada a cada categoría.

## Contenido

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos

Asegúrate de tener instalado Python y las dependencias necesarias. Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
## Instalación

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. **Configura un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    ```

3. **Activa el entorno virtual:**

   - En Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - En Linux/macOS:

     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```
    ## Uso

1. **Entrenamiento del Modelo:**

   - **Dataset:**
     - Asegúrate de tener el conjunto de datos de contraseñas etiquetadas en el archivo `data.csv`.

   - **Entrenamiento:**
     - Ejecuta el script de entrenamiento contenido en la carpeta data:

     ```bash
     python index.py
     ```

2. **Evaluación de Contraseñas:**

   - **Inferencia:**
     - Utiliza el modelo entrenado para evaluar la seguridad de una contraseña con la interfaz de usuario, para esto ejecuta el archivo de la carpeta raiz:

     ```bash
     python main.py
     ```

## Estructura del Proyecto

- `./app/`:
  - `__init__.py`
  - `gui.py`
  - `main.py`

- `./data/`:
  - `data.csv`
  - `index.py`
  - `modelo_RNN.h5`
  - `test.py`
  - `tokenizer.json`

- `./main.py`

- `./requirements.txt`


## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias de mejora, por favor crea un "issue" o envía una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
