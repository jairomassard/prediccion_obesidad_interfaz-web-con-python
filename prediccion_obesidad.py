import streamlit as st
import pandas as pd
import joblib


# Explicación del Código
# Este código permitirá crear una interfaz web simple donde los usuarios puedan ingresar sus datos y obtener una predicción del nivel de obesidad basado en el modelo que se entrenón de Machine Learning.

# Entradas del Usuario: El usuario puede ingresar valores para cada una de las características necesarias, como la edad, altura, peso, género, etc.
# Conversión de Datos: Los valores ingresados se convierten en un formato que el modelo puede interpretar.
# Predicción: Cuando se hace clic en el botón "Predecir Nivel de Obesidad", el modelo hace la predicción y muestra el resultado en la interfaz.



# Cargar el modelo previamente guardado y entrenado
modelo = joblib.load('modelo_obesidad.pkl')

def predecir_nivel_obesidad(modelo, input_data):
    X_nuevo = pd.DataFrame([input_data])
    prediccion = modelo.predict(X_nuevo)
    return prediccion[0]

# Título de la aplicación
st.title('Predicción de Nivel de Obesidad')

# Inputs de usuario
age = st.number_input('Edad', min_value=1, max_value=100, value=25)
height = st.number_input('Altura (en metros)', min_value=0.5, max_value=2.5, value=1.75)
weight = st.number_input('Peso (en kg)', min_value=1, max_value=200, value=70)
fcvc = st.slider('Frecuencia de consumo de vegetales FCVC (0-3)', 0, 3, 2)
ncp = st.slider('Número de comidas principales al día NCP', 1, 4, 3)
ch2o = st.slider('Litros de agua al día CH2O', 0, 3, 2)
faf = st.slider('Frecuencia de actividad física FAF', 0, 3, 2)
tue = st.slider('Horas de uso de tecnología al día TUE', 0, 5, 2)
gender = st.selectbox('Género', ['Masculino', 'Femenino'])
family_history = st.selectbox('Historial familiar de sobrepeso', ['Sí', 'No'])
favc = st.selectbox('Consumo frecuente de alimentos altos en calorías FAVC', ['Sí', 'No'])
caec = st.selectbox('Frecuencia de comer entre comidas CAEC', ['Frecuentemente', 'A veces', 'Nunca'])
smoke = st.selectbox('Usted Fuma', ['Sí', 'No'])
scc = st.selectbox('Monitorea las calorías que consume SCC', ['Sí', 'No'])
calc = st.selectbox('Frecuencia de consumo de alcohol CALC', ['Frecuentemente', 'A veces', 'Nunca'])
mtrans = st.selectbox('Transporte utilizado MTRANS', ['Automóvil', 'Moto', 'Bicicleta', 'Transporte público', 'Caminando'])

# Conversión de los inputs a formato de entrada del modelo
input_data = {
    'Age': age,
    'Height': height,
    'Weight': weight,
    'FCVC': fcvc,
    'NCP': ncp,
    'CH2O': ch2o,
    'FAF': faf,
    'TUE': tue,
    'Gender_Female': 1 if gender == 'Femenino' else 0,
    'Gender_Male': 1 if gender == 'Masculino' else 0,
    'family_history_with_overweight_no': 1 if family_history == 'No' else 0,
    'family_history_with_overweight_yes': 1 if family_history == 'Sí' else 0,
    'FAVC_no': 1 if favc == 'No' else 0,
    'FAVC_yes': 1 if favc == 'Sí' else 0,
    'CAEC_Always': 1 if caec == 'Siempre' else 0,
    'CAEC_Frequently': 1 if caec == 'Frecuentemente' else 0,
    'CAEC_Sometimes': 1 if caec == 'A veces' else 0,
    'CAEC_no': 1 if caec == 'Nunca' else 0,
    'SMOKE_no': 1 if smoke == 'No' else 0,
    'SMOKE_yes': 1 if smoke == 'Sí' else 0,
    'SCC_no': 1 if scc == 'No' else 0,
    'SCC_yes': 1 if scc == 'Sí' else 0,
    'CALC_Always': 1 if calc == 'Siempre' else 0,
    'CALC_Frequently': 1 if calc == 'Frecuentemente' else 0,
    'CALC_Sometimes': 1 if calc == 'A veces' else 0,
    'CALC_no': 1 if calc == 'Nunca' else 0,
    'MTRANS_Automobile': 1 if mtrans == 'Automóvil' else 0,
    'MTRANS_Bike': 1 if mtrans == 'Bicicleta' else 0,
    'MTRANS_Motorbike': 1 if mtrans == 'Moto' else 0,
    'MTRANS_Public_Transportation': 1 if mtrans == 'Transporte público' else 0,
    'MTRANS_Walking': 1 if mtrans == 'Caminando' else 0
}

# Predicción del modelo
#if st.button('Predecir Nivel de Obesidad'):
#    prediccion = predecir_nivel_obesidad(modelo, input_data)
#    st.write(f'Nivel de obesidad predicho: {prediccion}')

# Para ejecutar la aplicación, usa el siguiente comando en la terminal:
# streamlit run prediccion_obesidad.py

# Predicción del modelo
if st.button('Predecir Nivel de Obesidad'):
    prediccion = predecir_nivel_obesidad(modelo, input_data)
    
    # Estilizar el resultado de la predicción
    st.markdown(
        f"<div style='padding: 20px; border-radius: 10px; background-color: #4CAF50; color: white; text-align: center; font-size: 24px;'>"
        f"Nivel de obesidad predicho: <b>{prediccion}</b>"
        f"</div>",
        unsafe_allow_html=True
    )


# Para ejecutar la aplicación, se usa el siguiente comando en la terminal:
# streamlit run prediccion_obesidad.py