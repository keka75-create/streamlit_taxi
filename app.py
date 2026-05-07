import streamlit as st
import pandas as pd
import requests

st.title("Bienvenue Katarina! 👋")
st.write("Ceci est ma première app Streamlit!")

taxis = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv')

# Récupérer les quartiers (SANS NaN)
quartiers = sorted([q for q in taxis['pickup_zone'].unique() if pd.notna(q)])

quartier = st.selectbox("Choisissez un quartier :", quartiers)

st.write(f"Vous avez choisi {quartier}")

# Fonction pour récupérer une image Pexels
def get_pexels_image(query):
    search_query = f"{query} Manhattan street photography"
    url = f"https://api.pexels.com/v1/search?query={search_query}&per_page=1"  # ← Utilise search_query !
    headers = {"Authorization": "YcknU8b3WUjFgN40MIvgyUknjub7p4foRFyk4QSMeHUgR3jx3ZLgbyNu"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return data['photos'][0]['src']['medium']
    return None

# Afficher l'image
image = get_pexels_image(quartier)
if image:
    st.image(image)

st.subheader("Données des taxis")
st.write(taxis[taxis['pickup_zone'] == quartier].head(10))