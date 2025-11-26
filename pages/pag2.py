import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_all_data
(
    df # <- igual
) = load_all_data()
st.markdown("<h1 style='text-align: center;'>Visualizaciones y comparación</h1>", unsafe_allow_html=True)

def barra(df: pd.DataFrame):
    st.sidebar.header("Filtros")
    managers = st.sidebar.multiselect(
        "Selecciona Manager",
        options=sorted(df["Manager"].dropna().unique()),
        default=sorted(df["Manager"].dropna().unique())
    )

    categorias = st.sidebar.multiselect(
        "Filtra por categoría",
        options=sorted(df["Category"].dropna().unique()),
        default=sorted(df["Category"].dropna().unique())
    )
    return managers, categorias


def filtros(
    df: pd.DataFrame,
    managers: list,
    categorias: list
) -> pd.DataFrame:
    df_filtrado = df.copy()
    if managers:
        df_filtrado = df_filtrado[df_filtrado["Manager"].isin(managers)]
    if categorias:
        df_filtrado = df_filtrado[df_filtrado["Category"].isin(categorias)]
    return df_filtrado

MAN, CATEG = barra(df)
df_filtrado = filtros(df, MAN, CATEG)

st.subheader("Avance vs Presupuesto k$")

def grafica(df_filtrado):
    fig = px.scatter(
        df_filtrado,
        x="BudgetThousands",
        y="PercentComplete",
        color="State",
        hover_data=["ProjectName", "Manager"],
        title="Avance vs Presupuesto (k$)"
    )

    fig.update_layout(
        xaxis_title="budgethousands",
        yaxis_title="percentcomplete"
    )

    st.plotly_chart(fig, use_container_width=True)

grafica(df_filtrado)

