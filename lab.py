# %%



import pandas as pd 
import numpy as np

df = pd.read_csv('/home/lucaspoo/modulos/08_obesidad_sindrome_metabolico_mala.csv')  
df.head()

# %%

df.shape


# %%

df.info()

# informacion de las columnas y cuales tienen nulos teniendo la 7,8,9,10,11,12


# %%
# PRIMER ERRROR: Vemos que existen celdas en la columna de edades que no estan en un formato numerico

df[pd.to_numeric(df["Edad"], errors="coerce").isna()][["ID", "Edad"]]


# %%

# SEGUNDO PROBLEMA: observamos que para categorizar el genero del usuario se ocupan distintas variables
# pero siendo en realidad la variable de sexo biologico binaria, por lo que seria mas util que fuesen solo 2
#lo que dificulta la lectura y entendimiento
df["Sexo"].value_counts()


# %%
# TERCER PROBLEMA: Vemos que existen celdas en la columna de "Peso" que no estan en un formato numerico
#  lo que hace que los estos datos no puedan ser utilizados para analisis estadistico y de machine learning
df[pd.to_numeric(df["Peso"], errors="coerce").isna()][["ID", "Peso"]]


