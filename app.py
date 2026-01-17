import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith PRO", page_icon="🔫", layout="wide")

# --- LOGIN ---
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Parola incorectă!")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("LOGIN", on_click=verifica)

else:
    # --- MENIU LATERAL ---
    st.sidebar.title("NAVIGARE")
    meniu = st.sidebar.radio("Mergi la:", ["🔧 GUNSMITH (LIVE)", "🏠 LOBBY"])

    # --- DATLE ARME ---
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22"],
        "Marksman": ["M8A1", "Warden 308"],
        "Snipers": ["VS Recon", "Hawker HX"],
        "Shotguns": ["M10 Breacher"],
        "LMGs": ["Sokol 545"],
        "Pistols": ["Jäger 45"],
        "Specials": ["NX Ravager"]
    }

    # --- LISTA ATASAMENTE ---
    atasamente = {
        "Optic": ["Iron Sights", "Red Dot (+Acc)", "4x Scope (-Mob)", "Thermal"],
        "Muzzle": ["None", "Suppressor (-Range)", "Compensator (+Acc)"],
        "Barrel": ["Standard", "Long Barrel (+Range)", "Short Barrel (+Mob)"],
        "Underbarrel": ["None", "Vertical Grip (+Control)", "Ranger Grip (+Acc)"],
        "Magazine": ["Standard", "Fast Mag (+Reload)", "Extended Mag (-Mob)"],
        "Stock": ["Standard", "No Stock (+Mob)", "Heavy Stock (+Control)"],
        "Rear Grip": ["Standard", "Quickdraw (+Handling)", "Steady Aim (+Acc)"],
        "Fire Mod": ["Standard", "Rapid Fire (+Dmg)"]
    }

    if meniu == "🔧 GUNSMITH (LIVE)":
        st.title("🛠️ WEAPON GUNSMITH")
        
        # 1. SELECTIA ARMEI
        c1, c2 = st.columns(2)
        with c1:
            cat_p = st.selectbox("1. Categorie:", list(arsenal.keys()))
        with c2:
            weapon_p = st.selectbox("2. Arma:", arsenal[cat_p])
        
        st.markdown("---")

        # 2. INTERFATA SPLIT-SCREEN
        col_stanga, col_dreapta = st.columns([1.5, 1])

        with col_stanga:
            st.subheader("🔧 Atașamente")
            # Le punem direct, fara alte coloane imbricate, ca sa evitam erorile
            opt = st.selectbox("👁️ OPTIC", atasamente["Optic"])
            muz = st.selectbox("🔇 MUZZLE", atasamente["Muzzle"])
            bar = st.selectbox("📏 BARREL", atasamente["Barrel"])
            und = st.selectbox("✊ UNDERBARREL", atasamente["Underbarrel"])
            mag = st.selectbox("🔋 MAGAZINE", atasamente["Magazine"])
            stk = st.selectbox("🍑 STOCK", atasamente["Stock"])
            grp = st.selectbox("🧤 GRIP", atasamente["Rear Grip"])
            mod = st.selectbox("🔥 MOD", atasamente["Fire Mod"])

        # --- CALCULE MATEMATICE ---
        # Initializam variabilele
        fp = 50.0
        acc = 50.0
        mob = 50.0
        hnd = 50.0
        
        # Profil Arma (Base stats)
        if "Sniper" in cat_p: fp=90; mob=30; acc=80
        elif "SMG" in cat_p: fp=40; mob=85; hnd=80
        elif "Shotgun" in cat_p: fp=95; acc=20; mob=70
        elif "Assault" in cat_p: fp=60; acc=60; mob=60
        
        # Modificatori (Logica simplificata si sigura)
        # Verificam fiecare variabila pe rand
        if "No Stock" in stk: 
            mob += 20; acc -= 20; hnd -= 10
        if "
