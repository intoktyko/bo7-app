import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith PRO", page_icon="🔫", layout="wide")

# --- LOGIN SYSTEM ---
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
    st.button("CONNECT ONLINE SERVICES", on_click=verifica)

# --- APLICATIA PROPRIU-ZISA ---
else:
    # MENIU STÂNGA
    st.sidebar.markdown("### ≡ NAVIGARE JOC")
    meniu = st.sidebar.radio("Mergi la:", ["🏠 LOBBY", "🔫 WEAPONS & LOADOUTS", "🎫 BATTLE PASS", "🛒 STORE"])

    # BAZA DE DATE (Arsenal Complet)
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman": ["M8A1", "Warden 308", "M34 Novaline"],
        "Snipers": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI", "HEI-4"],
        "Specials": ["NX Ravager"],
        "Melee": ["Combat Knife", "Baseball Bat"]
    }

    # BAZA DE DATE ATASAMENTE
    atasamente = {
        "Optic": ["Iron Sights", "Merlin Mini", "Slate Reflex", "Red Dot", "Kobra Sight", "4x Acog", "Thermal Scope", "Variable Zoom"],
        "Muzzle": ["None", "Suppressor", "Compensator", "Muzzle Brake", "Flash Guard", "Breacher Device"],
        "Barrel": ["Standard", "Long Barrel", "Reinforced Barrel", "Match Grade", "Short Barrel", "Rapid Fire Barrel"],
        "Underbarrel": ["None", "Vertical Grip", "Ranger Foregrip", "Bipod", "Commando Grip", "Laser Sight", "Bruiser Grip"],
        "Magazine": ["Standard Mag", "Fast Mag", "Extended Mag I", "Extended Mag II", "Drum Mag", "High Caliber Rounds"],
        "Rear Grip": ["None", "Ergonomic Grip", "Quickdraw Grip", "Tape Grip", "Stippled Grip"],
        "Stock": ["None", "No Stock", "Heavy Stock", "Lightweight Stock", "Tactical Stock", "Collapsible Stock"],
        "Fire Mod": ["Standard", "Rapid Fire", "Burst Mod (3-Round)"]
    }

    # --- TAB WEAPONS ---
    if meniu == "🔫 WEAPONS & LOADOUTS":
        st.title("CREATE A CLASS")
        
        tab1, tab2 = st.tabs(["📂 LOADOUT PRINCIPAL", "🔧 GUNSMITH (ARMURIER)"])

        # TAB 1: PREZENTARE GENERALA
        with tab1:
            st.subheader("CUSTOM CLASS 1")
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown("### 🔫 PRIMARY WEAPON")
                cat_p = st.selectbox("Categorie:", list(arsenal.keys())[:-1], key="cat_p")
                weapon_p = st.selectbox("Arma:", arsenal[cat_p], key="weapon_p")
                st.info(f"Arma selectată: **{weapon_p}**")
            with c2:
                st.markdown("### 🃏 WILDCARD")
                st.selectbox("Card:", ["Overkill", "Gunfighter", "Perk Greed", "Danger Close"])
            
            st.write("---")
            st.info("💡 Mergi la tab-ul **GUNSMITH** de sus pentru a modifica accesoriile și a vedea statisticile!")

        # TAB 2: GUNSMITH CU CALCULE REALE
        with tab2:
            st.header(f"🔧 GUNSMITH: {weapon_p}")
            st.caption("Modifică atașamentele pentru a vedea cum se schimbă statisticile în dreapta.")

            col_parts, col_stats = st.columns([2, 1])
            
            with col_parts:
                # SELECTOARELE DE ATASAMENTE
                r1_a, r1_b = st.columns(2)
                with r1_a: opt = st.selectbox("👁️ OPTIC", atasamente["Optic"])
                with r1_b: muz = st.selectbox("🔇 MUZZLE", atasamente["Muzzle"])
                
                r2_a, r2_b = st.columns(2)
                with r2_a: bar = st.selectbox("📏 BARREL", atasamente["Barrel"])
                with r2_b: und = st.selectbox("✊ UNDERBARREL", atasamente["Underbarrel"])
                
                r3_a, r3_b = st.columns(2)
                with r3_a: mag = st.selectbox("🔋 MAGAZINE", atasamente["Magazine"])
                with r3_b: grp = st.selectbox("🧤 REAR GRIP", atasamente["Rear Grip"])
                
                r4_a, r4_b = st.columns(2)
                with r4_a: stk = st.selectbox("🍑 STOCK", atasamente["Stock"])
                with r4_b: mod = st.selectbox("🔥 FIRE MOD", atasamente["Fire Mod"])

            # --- MOTOR DE CALCUL STATISTICI ---
            # 1. Valori de baza in functie de clasa armei
            base_fp = 50
            base_acc = 50
            base_mob = 50
            base_hnd = 50

            if "Sniper" in cat_p: base_fp=90; base_acc=70; base_mob=20; base_hnd=30
            elif "Marksman" in cat_p: base_fp=75; base_acc=80; base_mob=40; base_hnd=45
            elif "SMG" in cat_p: base_fp=40; base_acc=40; base_mob=80; base_hnd=70
            elif "Shotgun" in cat_p: base_fp=85; base_acc=30; base_mob=60; base_hnd=60
            elif "LMG" in cat_p: base_fp=70; base_acc=60; base_mob=30; base_hnd=30
            elif "Assault" in cat_p: base_fp=60; base_acc=60; base_mob=50; base_hnd=50

            # 2. Modificari in functie de ATASAMENTELE selectate
            
            # MUZZLE
            if "Suppressor" in muz: base_fp -= 5; base_hnd += 5
            if "Compensator" in muz: base_acc += 10; base_hnd -= 5
            
            # BARREL
            if "Long Barrel" in bar: base_acc += 15; base_mob -= 10
            if "Short Barrel" in bar: base_mob += 10; base_acc -= 10
            if "Rapid Fire" in bar: base_fp += 10; base_acc -= 15

            # UNDERBARREL
            if "Vertical Grip" in und: base_acc += 8; base_hnd += 2
            if "Ranger" in und: base_acc += 12; base_mob -= 5
            if "Laser" in
