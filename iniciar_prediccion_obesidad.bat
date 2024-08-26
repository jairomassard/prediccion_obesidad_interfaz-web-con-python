@echo off
REM Cambia al directorio del proyecto
cd C:\Prediccion_obesidad

REM Activa el entorno virtual
call predecir_obesidad\Scripts\activate

REM Ejecuta Streamlit para lanzar la aplicación
streamlit run prediccion_obesidad.py

REM Mantén la ventana abierta después de que se cierre Streamlit
pause
