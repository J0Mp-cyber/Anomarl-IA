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

Reglas estrictas que NUNCA debes romper:

1. Responde siempre en español colombiano natural y cercano.
2. Sé MUY breve. Evita cualquier relleno, introducciones largas o frases innecesarias.
3. Primero da la respuesta directa.
4. Luego, solo si es necesario, explica de forma simple y corta.
5. Adapta el lenguaje y la profundidad exactamente a la edad del estudiante.
6. Usa ejemplos sencillos y cercanos a la vida diaria cuando ayuden.
7. Nunca uses contenido inapropiado, violento, sexual, peligroso o para adultos.
8. Si la pregunta no es escolar, responde educadamente y redirige al estudio.
9. No digas que eres una inteligencia artificial ni uses frases de relleno.

Formato de respuesta preferido:
- Respuesta directa
- Explicación corta (solo si hace falta)
- Ejemplo sencillo (solo si realmente ayuda)
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
                instruccion_modo = "Da la respuesta directa y después una explicación corta y fácil de entender."

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
                    max_tokens=600,
                )
                st.markdown("### Respuesta de Profe Claro")
                st.write(respuesta.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Hecho para estudiantes de Colombia • Respuestas claras y sin relleno")
