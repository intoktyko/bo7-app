import streamlit as st

st.set_page_config(page_title="BO7 Companion", page_icon="💀")

# --- PARTEA DE LOGIN ---
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    # Aici sunt userul si parola
    if st.session_state.user == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Greșit! Încearcă: sefu / admin123")

if not st.session_state.logat:
    st.title("🔒 Login War Room")
    st.text_input("User:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("Intră", on_click=verifica)

# --- PARTEA DE APLICATIE ---
else:
    st.title("💀 Black Ops 7 - War Room")
    if st.button("Ieșire (Logout)"):
        st.session_state.logat = False
        st.rerun()

    st.markdown("---")
    
    # Baza de date arme (scrisa pe mai multe randuri ca sa nu dea eroare)
    loadouts = {
        "XM4": {
            "Optic": "Merlin Mini", 
            "Muzzle": "Suppressor", 
            "Barrel": "Long Barrel"
        },
        "AK-74": {
            "Optic": "Iron Sights", 
            "Muzzle": "Compensator", 
            "Barrel": "Reinforced"
        }
    }

    optiune = st.sidebar.radio("Meniu:", ["Loadouts", "Statistici"])

    if optiune == "Loadouts":
        st.header("🔫 Configurează Arma")
        arma = st.selectbox("Alege:", list(loadouts.keys()))
        
        st.info(f"Setup pentru {arma}:")
        st.json(loadouts[arma]) # Afiseaza datele frumos

    elif optiune == "Statistici":
        st.header("📊 Calculator K/D")
        k = st.number_input("Kills", value=10)
        d = st.number_input("Deaths", value=5)
        if d > 0:
            st.metric("K/D Ratio", f"{k/d:.2f}")