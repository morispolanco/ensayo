import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue..")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

# Title
st.title('Genera un ensayo extenso a partir de las instrucciones')

# Instructions input
instructions = st.text_area('Instrucciones', height=100)

# Generate essay
if st.button('Generar ensayo'):
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=instructions,
        max_tokens=8000,
        
        n=1,
        stop=None,
        temperature=0.7
    )
    essay = response.choices[0].text.strip()
    st.markdown('## Ensayo generado')
    st.write(essay)
