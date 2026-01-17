import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith LIVE", page_icon="🎯", layout="wide")

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
        "Barrel": ["Standard", "Long Barrel (+Range/-Mob)", "Short Barrel (+Mob/-Acc)"],
        "Underbarrel": ["None", "Vertical Grip (+Control)", "Ranger Grip (+Acc)"],
        "Magazine": ["Standard", "Fast Mag (+Reload)", "Extended Mag (-Mob)"],
        "Stock": ["Standard", "No Stock (+Mob/-Control)", "Heavy Stock (+Control/-Mob)"],
        "Rear Grip": ["Standard", "Quickdraw (+Handling)", "Steady Aim (+Acc)"],
        "Fire Mod": ["Standard", "Rapid Fire (+Dmg/-Acc)"]
    }

    if meniu == "🔧 GUNSMITH (LIVE)":
        st.title("🛠️ WEAPON GUNSMITH")
        
        # 1. SELECTIA ARMEI (SUS)
        c_cat, c_weap = st.columns(2)
        with c_cat:
            cat_p = st.selectbox("1. Categorie:", list(arsenal.keys()))
        with c_weap:
            weapon_p = st.selectbox("2. Arma:", arsenal[cat_p])
        
        st.markdown("---")

        # 2. ZONA PRINCIPALA (SPLIT SCREEN)
        # Coloana 1 (Stanga): Atasamente
        # Coloana 2 (Dreapta): Statistici Live
        col_stanga, col_dreapta = st.columns([1.5, 1])

        with col_stanga:
            st.subheader("🔧 Configurează Atașamentele")
            # Folosim 'expander' ca sa arate curat, sau direct selectbox-uri
            
            c1, c2 = st.columns(2)
            with c1:
                opt = st.selectbox("👁️ OPTIC", atasamente["Optic"])
                muz = st.selectbox("🔇 MUZZLE", atasamente["Muzzle"])
                bar = st.selectbox("📏 BARREL", atasamente["Barrel"])
                und = st.selectbox("✊ UNDERBARREL", atasamente["Underbarrel"])
            with c2:
                mag = st.selectbox("🔋 MAGAZINE", atasamente["Magazine"])
                stk = st.selectbox("🍑 STOCK", atasamente["Stock"])
                grp = st.selectbox("🧤 GRIP", atasamente["Rear Grip"])
                mod = st.selectbox("🔥 MOD", atasamente["Fire Mod"])

        # --- CALCULELE SE FAC IN TIMP REAL AICI ---
        # Valori de baza
        fp = 50; acc = 50; mob = 50; hnd = 50
        
        # Profil Arma
        if "Sniper" in cat_p: fp=90; mob=30; acc=80
        if "SMG" in cat_p: fp=40; mob=85; hnd=80
        if "Shotgun" in cat_p: fp=95; acc=20; mob=70
        
        # Modificatori (Logica matematica)
        # Stock
        if "No Stock" in stk: mob += 20; acc -= 20; hnd -= 10
        if "Heavy Stock" in stk: acc += 15; mob -= 15
        # Barrel
        if "Long Barrel" in bar: acc += 15; mob -= 10
        if "Short Barrel" in bar: mob += 15; acc -= 15
        # Muzzle
        if "Suppressor" in muz: fp -= 5; hnd += 5
        if "Compensator" in muz: acc += 10; hnd -= 5
        # Underbarrel
        if "Vertical Grip" in und: acc += 8; hnd += 2
        if "Ranger Grip
