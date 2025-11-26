import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_all_data
(
    df # <- igual
) = load_all_data()
st.markdown("<h1 style='text-align: center;'>Dashboard principal de proyectos</h1>", unsafe_allow_html=True)


#funciones
def sidebar_filters_home(df: pd.DataFrame):
    st.sidebar.header("Filtros")
    estado = st.sidebar.selectbox(
        "Estado",
        options=["Todos"] + sorted(df["State"].dropna().unique()))
    categoria = st.sidebar.selectbox(
        "Categoría",options=["Todos"] + sorted(df["Category"].dropna().unique()))

    manager = st.sidebar.selectbox(
        "Manager",options=["Todos"] + sorted(df["Manager"].dropna().unique())
    )

    avmin = st.sidebar.slider(
        "Avance mínimo (%)",
        min_value=0,
        max_value=100,
        value=0
    )

    return estado, categoria, manager, avmin


def apply_filters_home(
    df: pd.DataFrame,
    estado: str,
    categoria: str,
    manager: str,
    min_avance: int
) -> pd.DataFrame:
   
    df_filtrado = df.copy()

    if estado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["State"] == estado]

    if categoria != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Category"] == categoria]

    if manager != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Manager"] == manager]

    df_filtrado = df_filtrado[df_filtrado["PercentComplete"] >= min_avance]

    return df_filtrado


estado, categoria, manager, min_avance = sidebar_filters_home(df)

df_filtrado = apply_filters_home(df, estado, categoria, manager, min_avance)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Proyectos", len(df_filtrado))

with col2:
    promedio = df_filtrado["PercentComplete"].mean() if len(df_filtrado) > 0 else 0
    st.metric("Promedio avance (%)", f"{promedio:.1f}")

with col3:
    st.metric("Managers únicos", df_filtrado["Manager"].nunique())

with col4:
    presupuesto = df_filtrado["BudgetThousands"].mean() if len(df_filtrado) > 0 else 0
    st.metric("Presupuesto medio", f"{presupuesto:.1f}K")

st.markdown("---")

st.dataframe(df_filtrado.head(10), use_container_width=True)

