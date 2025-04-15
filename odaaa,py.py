import streamlit as st
st.set_page_config(page_title="ODAAA", page_icon="😜", layout="centered")

st.title("ODAAA ¿quieres estar conmigo por mucho tiempo?")
st.write("Elige una de las siguientes opciones:")

opcion = st.radio(
    "Selecciona una respuesta:",
    ["Obeo si", "Obeo ño", "ÑOOO"]
)

if st.button("Enviar respuesta"):
    if opcion == "Obeo si":
        st.success("Muy bien!")
    elif opcion == "Obeo ño":
        st.error("okey ve con el niño tripita y palau 😭.")
    elif opcion == "ÑOOO"
        st.error("ELIGE OTRA VEZ 😡😡😡")