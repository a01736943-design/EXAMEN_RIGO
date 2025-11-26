import streamlit as st
import plotly.io as pio

st.set_page_config(
    page_title="Dashboard Principal",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

airbnb_colorway = [
    "#FF5A5F",  # Coral principal
    "#00A699",  # Aqua
    "#484848",  # Gris oscuro
    "#FC642D",  # Naranja
    "#F2C94C",  # Amarillo suave
]

airbnb_sequential = [
    "#F7F3F2",
    "#FAD9D6",
    "#FF7A81",
    "#DE1C40"
]

# Definición del template
custom_theme = dict(
    layout=dict(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        colorway=airbnb_colorway,
        coloraxis=dict(
            colorscale=airbnb_sequential
        )))

pio.templates["airbnb_pro"] = custom_theme
pio.templates.default = "airbnb_pro"


pg_extraccion = st.Page("pages/pag1.py", title="home", icon="👽")
pg_tablas = st.Page("pages/pag2.py", title="Analisis de proyectos",icon="🫡")


nav = st.navigation(
    {
        "Inicio": [pg_extraccion],
        "Visualización": [pg_tablas],
    }
)

nav.run()