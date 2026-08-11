# Como correr el proyecto

Ejecutando la siguiente sucesión de comandos deberían poder dejar corriendo esto en su computador. Preferí usar esta estructura local ya que no me gusta Google Colab. 

> **Nota:** Se recomienda añadir la extensión de **Jupyter** a VS Code para poder visualizar los DataFrames de forma interactiva.

## Pasos de instalación

```bash
# 1. Clonar y entrar a la carpeta
git clone https://github.com/lucaspoor/dataframe-lab.git
cd dataframe-lab

# 2. Crear un .venv nuevo y limpio
python -m venv .venv

# 3. Activar el entorno
source .venv/bin/activate

# 4. Reinstalar todas las librerías desde el archivo
pip install -r requirements.txt
