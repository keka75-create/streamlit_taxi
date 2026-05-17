import streamlit as st
import pandas as pd

# Charger les données
taxis = pd.read_csv('taxis.csv')

st.title("🚕 Bienvenue Katarina! 👋")
st.write("Ceci est ma première app Streamlit!")

# Images associées
images = {
    'Times Sq/Theatre District': 'img/time square.jpg',
    'SoHo': 'img/soho.jpg',
    'West Village': 'img/west village.jpg',
    'Williamsburg (North Side)': 'img/williamsburg-bridge-147104085-58f7ee2f3df78ca1598bd7c9.jpg',
    'Park Slope': 'img/park slop.jpg'
}

# Les 5 quartiers
quartiers = list(images.keys())

quartier = st.selectbox("Choisissez un quartier :", quartiers)
st.write(f"Vous avez choisi **{quartier}**")

# Afficher l'image
st.image(images[quartier])

# Tableau données
st.subheader("Données des taxis")
st.write(taxis[taxis['pickup_zone'] == quartier].head(10))

# DASHBOARD INTERACTIF
st.title("📊 Dashboard Interactif")

colonnes = taxis.select_dtypes(include='number').columns.tolist()
col_x = st.selectbox("Choisissez la colonne X :", colonnes)
col_y = st.selectbox("Choisissez la colonne Y :", colonnes)

graphique = st.selectbox("Choisissez un graphique :", ['scatter_chart', 'bar_chart', 'line_chart'])

# Limiter à 500 lignes
df_graph = taxis[[col_x, col_y]].dropna().head(500)

if graphique == 'scatter_chart':
    st.scatter_chart(df_graph)
elif graphique == 'bar_chart':
    st.bar_chart(df_graph)
elif graphique == 'line_chart':
    st.line_chart(df_graph)

# Matrice de corrélation
if st.checkbox("Afficher la matrice de corrélation"):
    df_numerique = taxis.select_dtypes(include='number')
    st.write(df_numerique.corr())
