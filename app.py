import pandas as pd 
import streamlit as st 

st.title("Aplicativo para el manejo de datos incompletos")
st.title("Data original")

df= pd.read_excel("mu_enoe_NAN.xlsx")
st.write(df)

conteo_nan =df.isna().sum()
st.write (conteo_nan)

st.title("Dropna") #este borra las filas con celdas vacias de una cumna especifica
df_limpio = df.dropna(subset=["ingreso_mensual"])
st.write(df_limpio)

conteo_df_limpio =df_limpio.isna().sum()
st.write (conteo_df_limpio)


st.title("ffill")
df_fill_na_f= df.fillna(method="ffill") #rellena los datos automaticamente con el ultimo ultimo numeto valido de arriba
st.write (df_fill_na_f)

df_fill_na_f= df_fill_na_f.isna().sum()
st.write (df_fill_na_f)

st.title("bfill")
df_fill_na_f= df.fillna(method="bfill") #rellena los datos automaticamente con el ultimo ultimo numeto valido de abajo
st.write (df_fill_na_f)

df_fill_na_f= df_fill_na_f.isna().sum()
st.write (df_fill_na_f)

st.title("mean")
df_fill_mean= df.fillna(df.mean(numeric_only=True)) #rellena con el promedio de los valores de la columna
st.write (df_fill_mean)

df_fill_mean= df_fill_mean.isna().sum()
st.write (df_fill_mean)
