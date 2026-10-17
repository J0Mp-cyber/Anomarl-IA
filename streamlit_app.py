import streamlit as st
from groq import Groq

# Configuración de la página
st.set_page_config(
    page_title="Profe Claro",
    page_icon="📚",
    layout="centered"
)

st.title("Profe Claro")
st.markdown("### IA escolar clara, rápida y sin relleno")
st.caption("Especializada para estudiantes de Colombia")

# Cliente de Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

SYSTEM_PROMPT = """Eres "Profe Claro", una IA escolar especializada en ayudar a estudiantes de Colombia.

Reglas importantes:

1. Responde siempre en español colombiano natural.
2. Sé claro y completo, pero sin relleno innecesario.
3. Primero da la respuesta directa.
4. Después muestra los pasos de forma ordenada y completa (especialmente en matemáticas).
5. No te saltes pasos importantes.
6. Adapta el lenguaje según la edad del estudiante.
7. Usa un formato limpio y fácil de leer.
8. Nunca uses contenido inapropiado.
9. No digas que eres una inteligencia artificial.

Formato preferido de respuesta:

**Respuesta:**
(aquí la respuesta final)

**Paso a paso:**
1. ...
2. ...
3. ...

(Si es matemáticas, muestra las operaciones claramente)
"""

# Interfaz
edad = st.selectbox(
    "¿Cuál es tu edad?",
    ["8-10 años", "11-13 años", "14-15 años", "16-17 años"],
    index=2
)

modo = st.radio(
    "¿Cómo quieres la ayuda?",
    ["Solo respuesta", "Explicación corta"],
    horizontal=True
)

pregunta = st.text_area(
    "Tu pregunta",
    placeholder="Escribe tu pregunta de matemáticas, ciencias, sociales, español...",
    height=100
)

if st.button("Preguntar", type="primary"):
    if not pregunta.strip():
        st.warning("Escribe una pregunta para poder ayudarte.")
    else:
        with st.spinner("Pensando..."):
            if edad == "8-10 años":
                nivel = "Explica como si hablaras con un niño de primaria. Usa palabras muy simples y ejemplos de la vida diaria."
            elif edad == "11-13 años":
                nivel = "Explica de forma clara y sencilla, como para un estudiante de sexto a octavo."
            elif edad == "14-15 años":
                nivel = "Explica de forma clara y directa, como para un estudiante de noveno o décimo."
            else:
                nivel = "Explica de forma clara, precisa y concisa, como para un estudiante de undécimo o bachillerato."

            if modo == "Solo respuesta":
                instruccion_modo = "Da ÚNICAMENTE la respuesta directa. No expliques nada más."
            else:
                instruccion_modo = "Da la respuesta directa y después una explicación completa y ordenada paso a paso."

            mensajes = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Edad del estudiante: {edad}\n{nivel}\nModo: {instruccion_modo}\n\nPregunta del estudiante: {pregunta}"
                }
            ]

            try:
                respuesta = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=mensajes,
                    temperature=0.4,
                    max_tokens=1000,
                )
                st.markdown("### Respuesta de Profe Claro")
                st.write(respuesta.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Hecho para estudiantes de Colombia • Respuestas claras y sin relleno")
