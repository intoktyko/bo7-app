import streamlit as st
import time

# ==========================================
# 1. CONFIGURARE PAGINĂ
# ==========================================
st.set_page_config(page_title="BO7 ULTIMATE", page_icon="💀", layout="wide")

# ==========================================
# 2. INITIALIZARE SESIUNE (PROTECTIE ANTI-EROARE)
# ==========================================
# Aici ne asiguram ca variabilele exista inainte sa le folosim
if 'logat' not in st.session_state:
    st.session_state.logat = False
if 'user' not in st.session_state:
    st.session_state.user = "Operator"

# ==========================================
# 3. SISTEM DE LOGIN
# ==========================================
def verifica_parola():
    # Folosim .get pentru siguranta maxima
    u = st.session_state.get("input_user", "")
    p = st.session_state.get("input_parola", "")
    
    if u.lower() == "sefu" and p == "admin123":
        st.session_state.logat = True
        st.session_state.user = u
        # Am scos st.toast pentru compatibilitate
    else:
        st.error("❌ EROARE: Date incorecte!")

if not st.session_state.logat:
    st.markdown("<h1 style='text-align: center;'>🔒 BO7 COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("---")
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.info("Introduceți credențialele:")
        st.text_input("Operativ:", key="input_user")
        st.text_input("Cod Acces:", type="password", key="input_parola")
        st.button("🔴 CONECTARE", on_click=verifica_parola)

# ==========================================
# 4. APLICATIA PROPRIU-ZISA (DOAR DACA E LOGAT)
# ==========================================
else:
    # Sidebar
    st.sidebar.title("NAVIGARE")
    meniu = st.sidebar.radio("Meniu:", 
        ["🏠 LOBBY", "🔫 WEAPONS & LOADOUTS", "🎫 BATTLE PASS", "🛒 STORE"])
    
    # Afisam userul curent cu protectie
    user_curent = st.session_state.get('user', 'SEFU').upper()
    st.sidebar.success(f"🟢 ONLINE: {user_curent}")
    
    # --- BAZA DE DATE ARSENAL ---
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0", "X9 Maverick"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman": ["M8A1", "Warden 308", "M34 Novaline"],
        "Snipers": ["VS Recon", "Hawker HX", "Shadow SK"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI"],
        "Specials": ["NX Ravager"],
        "Melee": ["Combat Knife", "Baseball Bat"]
    }

    # --- LISTA ATASAMENTE ---
    atasamente = {
        "Optic": ["Iron Sights", "Red Dot (+Acc)", "4x Acog (-Mob)", "Thermal Scope", "Variable Zoom"],
        "Muzzle": ["None", "Suppressor (-Range)", "Compensator (+Acc)", "Muzzle Brake (+Ctrl)"],
        "Barrel": ["Standard", "Long Barrel (+Range)", "Reinforced (+Dmg)", "Short Barrel (+Mob)"],
        "Underbarrel": ["None", "Vertical Grip (+Ctrl)", "Ranger Foregrip (+Acc)", "Laser Sight"],
        "Magazine": ["Standard", "Fast Mag (+Rld)", "Extended Mag (-Mob)", "Drum Mag (-Mob)"],
        "Rear Grip": ["None", "Quickdraw (+Hnd)", "Tape Grip", "Ergonomic Grip"],
        "Stock": ["Standard", "No Stock (+Mob/-Acc)", "Heavy Stock (+Acc)", "Tactical Stock"],
        "Fire Mod": ["Standard", "Rapid Fire (+Rate)", "Burst Mod"]
    }

    # --- PAGINA GUNSMITH ---
    if meniu == "🔫 WEAPONS & LOADOUTS":
        st.title("🛠️ GUNSMITH SYSTEM")
        
        # Selectie Arma
        col1, col2 = st.columns([1, 2])
        with col1:
            cat_p = st.selectbox("CATEGORIE:", list(arsenal.keys()))
        with col2:
            weapon_p = st.selectbox("ARMA:", arsenal[cat_p])

        st.markdown("---")
        st.subheader(f"🔧 Configurare: {weapon_p}")
        
        # Split Screen: Piese (Stanga) vs Stats (Dreapta)
        c_parts, c_stats = st.columns([1.5, 1])

        with c_parts:
            # 8 Sloturi
            r1a, r1b = st.columns(2)
            with r1a: opt = st.selectbox("👁️ OPTIC", atasamente["Optic"])
            with r1b: muz = st.selectbox("🔇 MUZZLE", atasamente["Muzzle"])
            
            r2a, r2b = st.columns(2)
            with r2a: bar = st.selectbox("📏 BARREL", atasamente["Barrel"])
            with r2b: und = st.selectbox("✊ UNDERBARREL", atasamente["Underbarrel"])
            
            r3a, r3b = st.columns(2)
            with r3a: mag = st.selectbox("🔋 MAGAZINE", atasamente["Magazine"])
            with r3b: grp = st.selectbox("🧤 REAR GRIP", atasamente["Rear Grip"])
            
            r4a, r4b = st.columns(2)
            with r4a: stk = st.selectbox("🍑 STOCK", atasamente["Stock"])
            with r4b: mod = st.selectbox("🔥 FIRE MOD", atasamente["Fire Mod"])

        # CALCULATOR SIMPLU (FARA ERORI DE LOGICA)
        fp = 50; acc = 50; mob = 50; hnd = 50

        # Base Stats
        if "Sniper" in cat_p: fp=90; acc=80; mob=20
        elif "SMG" in cat_p: fp=40; acc=40; mob=85
        elif "Shotgun" in cat_p: fp=90; acc=20; mob=70
        
        # Modificatori (Logica If simpla)
        if "Long" in bar: acc += 15; mob -= 10
        if "Short" in bar: mob += 15; acc -= 10
        if "No Stock" in stk: mob += 20; acc -= 20
        if "Heavy" in stk: acc += 15; mob -= 15
        if "Suppressor" in muz: fp -= 5
        if "Extended" in mag: mob -= 10
        if "Rapid" in mod: fp += 15; acc -= 10

        # Limitare 0-100
        fp = max(0, min(100, fp))
        acc = max(0, min(100, acc))
        mob = max(0, min(100, mob))
        hnd = max(0, min(100, hnd))

        with c_stats:
            st.markdown("### 📊 STATISTICI")
            st.write(f"Firepower: {fp}")
            st.progress(fp/100)
            st.write(f"Accuracy: {acc}")
            st.progress(acc/100)
            st.write(f"Mobility: {mob}")
            st.progress(mob/100)
            st.write(f"Handling: {hnd}")
            st.progress(hnd/100)

        # Restul Loadout-ului
        st.markdown("---")
        st.subheader("🎒 ECHIPAMENT EXTRA")
        c_s, c_p, c_w = st.columns(3)
        with c_s:
            st.selectbox("Secondary", ["Jäger 45", "Launcher"])
            st.selectbox("Lethal", ["Frag", "Semtex", "C4"])
        with c_p:
            st.selectbox("Perk 1", ["Ghost", "Flak Jacket"])
            st.selectbox("Perk 2", ["Fast Hands", "Tracker"])
            st.selectbox("Perk 3", ["Dexterity", "Double Time"])
        with c_w:
            st.selectbox("Wildcard", ["Overkill", "Gunfighter"])
            st.selectbox("Field Upgrade", ["Trophy System", "Assault Pack"])

    # --- LOBBY ---
    elif meniu == "🏠 LOBBY":
        st.title("MULTIPLAYER LOBBY")
        col_lob1, col_lob2 = st.columns([2,1])
        with col_lob1:
            st.subheader("FIND MATCH")
            st.write("Playlist: **Nuketown 24/7**")
            if st.button("START MATCHMAKING"):
                with st.spinner("Cautare meci..."):
                    time.sleep(1.5)
                st.success("Meci Gasit! Connecting...")
        with col_lob2:
            st.warning(f"Player: {user_curent}")
            st.write("Level 55 (Prestige 1)")

    # --- BATTLE PASS ---
    elif meniu == "🎫 BATTLE PASS":
        st.title("BATTLE PASS SEZON 1")
        st.progress(0.45, text="Progres: 45%")
        st.info("Rewards Available: 2")

    # --- STORE ---
    elif meniu == "🛒 STORE":
        st.title("STORE")
        st.write("Featured: Goliath Pack")
        # Exemplu de buton donatie (fara link real momentan)
        st.markdown("---")
        st.subheader("💰 Susține Dezvoltatorul")
        st.info("Dacă vrei să transformăm asta într-o aplicație plătită, apasă mai jos.")
        st.button("Donație (Demo)")

    # LOGOUT
    st.sidebar.markdown("---")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logat = False
        st.session_state.user = "Operator"
        st.rerun()
