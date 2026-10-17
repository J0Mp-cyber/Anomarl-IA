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
