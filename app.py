import streamlit as st

st.set_page_config(page_title="BO7 META ARSENAL", page_icon="🔥", layout="wide")

if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Date incorecte!")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room Login")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("Accesează Arsenalul", on_click=verifica)
else:
    st.sidebar.title("🎮 Meniu Tactic")
    pagina = st.sidebar.radio("Navigare:", ["🔥 Top 3 Meta", "🔫 Toate Armele (Builds)", "🏆 Camo Tracker"])

    # Baza de date cu Top 3 si Atasamente
    meta_data = {
        "Assault Rifles": {
            "Maddox RFB": {"rating": "9.8/10", "top": True, "build": ["Reflex Sight", "Long Barrel", "Vertical Grip", "Fast Mag", "Quickdraw Stock"]},
            "AK-27": {"rating": "9.5/10", "top": True, "build": ["Compensator", "Heavy Barrel", "Ranger Foregrip", "Extended Mag", "Recoil Pad"]},
            "MXR-17": {"rating": "9.2/10", "top": True, "build": ["Red Dot", "Reinforced Barrel", "Commando Grip", "Fast Mag", "Ergonomic Grip"]},
            "M15 MOD 0": {"rating": "8.5/10", "top": False, "build": ["Reflex", "Suppressed Barrel", "Vertical Grip", "Extended Mag", "Steady Stock"]}
        },
        "Marksman Rifles": {
            "M8A1": {"rating": "9.9/10", "top": True, "build": ["4x Optic", "Match Grade Barrel", "Bipod Grip", "High Caliber Rounds", "Heavy Stock"]},
            "Warden 308": {"rating": "9.4/10", "top": True, "build": ["Thermal Scope", "Long Barrel", "Vertical Grip", "Extended Mag", "Quickdraw"]},
            "M34 Novaline": {"rating": "9.0/10", "top": True, "build": ["Red Dot", "Rapid Fire", "Ranger Grip", "Fast Mag", "Steady Stock"]}
        },
        "SMGs": {
            "Jackal PDW": {"rating": "9.7/10", "top": True, "build": ["No Stock", "Short Barrel", "Laser Sight", "Fast Mag", "Ergonomic Grip"]},
            "C9": {"rating": "9.3/10", "top": True, "build": ["Suppressor", "Long Barrel", "Vertical Grip", "Extended Mag", "Recoil Pad"]},
            "KSV": {"rating": "9.1/10", "top": True, "build": ["Reflex", "Rapid Fire", "Ranger Grip", "Fast Mag", "Lightweight Stock"]}
        }
    }

    if pagina == "🔥 Top 3 Meta":
        st.header("🏆 Top 3 Arme pe Categorie")
        for cat, arme in meta_data.items():
            with st.expander(f"Top {cat}"):
                top_3 = [name for name, d in arme.items() if d["top"]]
                for i, name in enumerate(top_3[:3]):
                    st.write(f"*{i+1}. {name}* - Rating: {arme[name]['rating']}")

    elif pagina == "🔫 Toate Armele (Builds)":
        st.header("Cele mai bune Clase (Builds)")
        cat_sel = st.selectbox("Categorie:", list(meta_data.keys()))
        arma_sel = st.selectbox("Arma:", list(meta_data[cat_sel].keys()))
        
        info = meta_data[cat_sel][arma_sel]
        st.subheader(f"Configurația Meta pentru {arma_sel}")
        st.write(f"⭐ *Rating: {info['rating']}*")
        
        st.markdown("### 🔧 Cele 5 Atașamente Obligatorii:")
        for at in info["build"]:
            st.write(f"✅ {at}")
        
        st.info("💡 Această clasă este optimizată pentru maximizarea daunelor și controlul reculului.")

    elif pagina == "🏆 Camo Tracker":
        st.header("Progres Camuflaje")
        st.checkbox("Gold unlocked")
        st.checkbox("Diamond unlocked")

    if st.sidebar.button("Logout"):
        st.session_state.logat = False
        st.rerun()
