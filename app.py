import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith FIXED", page_icon="🛠️", layout="wide")

# --- LOGIN ---
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Parola greșită!")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("LOGIN", on_click=verifica)

else:
    # --- AICI ESTE CODUL PRINCIPAL ---
    
    # 1. DEFINIM DATELE PRIMA DATA (Ca sa nu dea eroare "Not Found")
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman": ["M8A1", "Warden 308", "M34 Novaline"],
        "Snipers": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI"],
        "Melee": ["Combat Knife", "Baseball Bat"]
    }

    atasamente = {
        "Optic": ["Iron Sights", "Merlin Mini", "Slate Reflex", "Red Dot", "Kobra Sight", "4x Acog", "Thermal"],
        "Muzzle": ["None", "Suppressor", "Compensator", "Muzzle Brake"],
        "Barrel": ["Standard", "Long Barrel", "Reinforced Barrel", "Short Barrel"],
        "Underbarrel": ["None", "Vertical Grip", "Ranger Foregrip", "Commando Grip"],
        "Magazine": ["Standard Mag", "Fast Mag", "Extended Mag", "Drum Mag"],
        "Rear Grip": ["None", "Ergonomic Grip", "Quickdraw Grip", "Tape Grip"],
        "Stock": ["None", "No Stock", "Heavy Stock", "Lightweight Stock"],
        "Fire Mod": ["Standard", "Rapid Fire"]
    }

    # 2. MENIUL LATERAL
    st.sidebar.title("NAVIGARE")
    meniu = st.sidebar.radio("Mergi la:", ["🏠 LOBBY", "🔫 LOADOUTS & GUNSMITH", "🎫 BATTLE PASS"])

    # 3. PAGINA LOADOUTS (Aici era problema)
    if meniu == "🔫 LOADOUTS & GUNSMITH":
        st.title("CREATE A CLASS")
        
        # Selectoarele principale
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("1. Alege Categoria")
            # Afisam TOATE categoriile, fara filtre, ca sa fim siguri ca apar
            cat_p = st.selectbox("Categorie:", list(arsenal.keys()))
        
        with col2:
            st.subheader("2. Alege Arma")
            # Luam armele din categoria aleasa mai sus
            if cat_p:
                weapon_p = st.selectbox("Arma:", arsenal[cat_p])
            else:
                st.warning("Alege o categorie!")

        st.markdown("---")
        
        # TAB-URI PENTRU GUNSMITH
        tab1, tab2 = st.tabs(["🔧 CONFIGURARE (Gunsmith)", "📊 STATISTICI"])
        
        with tab1:
            st.write(f"Modifică atașamentele pentru: **{weapon_p}**")
            c1, c2 = st.columns(2)
            with c1:
                opt = st.selectbox("👁️ Optic", atasamente["Optic"])
                muz = st.selectbox("🔇 Muzzle", atasamente["Muzzle"])
                bar = st.selectbox("📏 Barrel", atasamente["Barrel"])
                und = st.selectbox("✊ Underbarrel", atasamente["Underbarrel"])
            with c2:
                mag = st.selectbox("🔋 Magazine", atasamente["Magazine"])
                grp = st.selectbox("🧤 Rear Grip", atasamente["Rear Grip"])
                stk = st.selectbox("🍑 Stock", atasamente["Stock"])
                mod = st.selectbox("🔥 Fire Mod", atasamente["Fire Mod"])

        with tab2:
            st.subheader("Simulare Statistici")
            # Valori de baza
            fp = 50; acc = 50; mob = 50; hnd = 50
            
            # Calcule simple
            if "Sniper" in cat_p: fp=90; mob=20
            if "SMG" in cat_p: mob=80; fp=40
            
            if "No Stock" in stk: mob += 20; acc -= 20
            if "Long Barrel" in bar: acc += 15; mob -= 10
            if "Suppressor" in muz: fp -= 5
            
            # Afisare
            st.write("Firepower"); st.progress(min(max(fp/100, 0.0), 1.0))
            st.write("Accuracy"); st.progress(min(max(acc/100, 0.0), 1.0))
            st.write("Mobility"); st.progress(min(max(mob/100, 0.0), 1.0))
            st.write("Handling"); st.progress(min(max(hnd/100, 0.0), 1.0))

    elif meniu == "🏠 LOBBY":
        st.title("MULTIPLAYER LOBBY")
        st.button("FIND MATCH")

    elif meniu == "🎫 BATTLE PASS":
        st.title("BATTLE PASS")

    # LOGOUT
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state.logat = False
        st.rerun()
