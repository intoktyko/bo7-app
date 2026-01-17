import streamlit as st

st.set_page_config(page_title="BO7 WAR ROOM", page_icon="🔥", layout="wide")

# Login
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Acces Respins!")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room Login")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("Intră în Arsenal", on_click=verifica)
else:
    st.sidebar.title("🎮 Meniu Multiplayer")
    pagina = st.sidebar.radio("Navighează:", ["🏆 TOP 3 META", "🔫 Arsenal Complet", "🏅 Tracker Camo"])

    # Baza de date din pozele tale
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "M15 MOD 0", "AK-27", "MXR-17", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["C9", "KSV", "Tanto .22", "Jackal PDW", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman Rifles": ["M8A1", "Warden 308", "M34 Novaline"],
        "Sniper Rifles": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI", "HEI-4"],
        "Specials": ["NX Ravager"]
    }

    # --- PAGINA 1: TOP 3 META ---
    if pagina == "🏆 TOP 3 META":
        st.header("🔥 Cele mai bune 3 arme din fiecare categorie")
        st.write("Acestea sunt armele care domină meta-ul actual:")
        
        c1, c2 = st.columns(2)
        with c1:
            with st.expander("🥇 TOP 3 Assault Rifles"):
                st.write("1. *Maddox RFB* (Build: Reflex, Long Barrel, Vertical Grip, Fast Mag, Quickdraw Stock)")
                st.write("2. *AK-27* (Build: Compensator, Heavy Barrel, Ranger Grip, Extended Mag, Recoil Pad)")
                st.write("3. *MXR-17* (Build: Red Dot, Reinforced Barrel, Commando Grip, Fast Mag, Ergonomic Grip)")
            
            with st.expander("🥇 TOP 3 SMGs"):
                st.write("1. *Jackal PDW* (Build: No Stock, Short Barrel, Laser, Fast Mag, Ergonomic Grip)")
                st.write("2. *C9* (Build: Suppressor, Long Barrel, Vertical Grip, Extended Mag, Recoil Pad)")
                st.write("3. *KSV* (Build: Reflex, Rapid Fire, Ranger Grip, Fast Mag, Lightweight Stock)")

        with c2:
            with st.expander("🥇 TOP 3 Marksman/Sniper"):
                st.write("1. *M8A1* (Build: 4x Optic, Match Grade Barrel, Bipod Grip, High Caliber, Heavy Stock)")
                st.write("2. *VS Recon* (Build: Variable Zoom, Reinforced Barrel, Bipod, Fast Mag, Heavy Stock)")
                st.write("3. *Warden 308* (Build: Thermal, Long Barrel, Vertical Grip, Extended Mag, Quickdraw)")

    # --- PAGINA 2: ARSENAL COMPLET ---
    elif pagina == "🔫 Arsenal Complet":
        st.header("🗃️ Toate armele pe categorii")
        cat_sel = st.selectbox("Alege Categoria:", list(arsenal.keys()))
        arma_sel = st.selectbox("Vezi Arma:", arsenal[cat_sel])
        
        st.subheader(f"Informații: {arma_sel}")
        if arma_sel in ["Maddox RFB", "M8A1", "Warden 308", "Jäger 45"]:
            st.success("Statut: MAX LEVEL (Bravo, șefu'!)")
        st.write("Aici poți adăuga note personale sau loadout-uri secundare pentru această armă.")

    # --- PAGINA 3: CAMO ---
    elif pagina == "🏅 Tracker Camo":
        st.header("🏆 Progres Master Camo")
        st.checkbox("Mastery: GOLD", value=True)
        st.checkbox("Mastery: DIAMOND")
        st.checkbox("Special: ELEVATE (Universal)", value=True)

    if st.sidebar.button("Logout"):
        st.session_state.logat = False
        st.rerun()
