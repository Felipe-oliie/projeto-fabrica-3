import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fábrica de Jovem Aprendiz", layout="wide")

# Fundo preto via CSS
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #222222;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("Fábrica de Jovem Aprendiz 🏭")
st.markdown("### Compare o preço do seu produto com os mercados locais:")

# Entrada de dados do usuário
produto = st.text_input("Digite o nome do produto (ex.: Arroz 5kg):")
preco_usuario = st.number_input("Preço que você pagou (R$):", min_value=0.0, format="%.2f")

st.markdown("### Preços nos outros mercados:")
mercado1 = st.number_input("Mercado 1 (R$):", min_value=0.0, format="%.2f")
mercado2 = st.number_input("Mercado 2 (R$):", min_value=0.0, format="%.2f")
mercado3 = st.number_input("Mercado 3 (R$):", min_value=0.0, format="%.2f")

# Botão de comparação
if st.button("Comparar"):
    if not produto:
        st.error("Informe o nome do produto.")
    else:
        # Criar DataFrame
        mercados = ["Você pagou", "Mercado 1", "Mercado 2", "Mercado 3"]
        precos = [preco_usuario, mercado1, mercado2, mercado3]
        df = pd.DataFrame({"Mercado": mercados, "Preço (R$)": precos})
        
        # Destacar o menor preço
        menor_preco = df["Preço (R$)"].min()
        df["Mais barato"] = df["Preço (R$)"].apply(lambda x: "✅" if x == menor_preco else "")
        
        # Mostrar tabela
        st.subheader(f"Comparação de preços para: {produto}")
        st.table(df)
