import streamlit as st
import time

# ==========================================
# 1. CONFIGURARE PAGINĂ & STIL
# ==========================================
st.set_page_config(page_title="BO7 ULTIMATE COMMAND", page_icon="💀", layout="wide")

# ==========================================
# 2. SISTEM DE LOGIN (REPARAT)
# ==========================================
# Aici era problema: Inițializăm variabilele de la bun început
if 'logat' not in st.session_state:
    st.session_state.logat = False
if 'user' not in st.session_state:
    st.session_state.user = ""

def verifica_parola():
    # Folosim direct valorile introduse in input
    # Accesam widget-urile prin key
    username_input = st.session_state.input_user
    password_input = st.session_state.input_parola
    
    if username_input.lower() == "sefu" and password_input == "admin123":
        st.session_state.logat = True
        st.session_state.user = username_input # Salvam explicit utilizatorul
        st.toast("✅ Acces Aprobat! Bine ai venit, Șefu'!")
    else:
        st.error("❌ EROARE: Date incorecte!")

if not st.session_state.logat:
    st.markdown("<h1 style='text-align: center;'>🔒 BO7 COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("---")
    col_login1, col_login2, col_login3 = st.columns([1, 2, 1])
    with col_login2:
        st.info("Introduceți credențialele de acces:")
        # Am schimbat key-urile ca sa nu se confunde cu variabila de sesiune
        st.text_input("Operativ (User):", key="input_user")
        st.text_input("Cod Securitate (Pass):", type="password", key="input_parola")
        st.button("🔴 INIȚIALIZARE SISTEM", on_click=verifica_parola, use_container_width=True)

# ==========================================
# 3. INTERFAȚA PRINCIPALĂ (DUPĂ LOGIN)
# ==========================================
else:
    # --- MENIU LATERAL (SIDEBAR) ---
    st.sidebar.title("NAVIGARE TACTICĂ")
    st.sidebar.markdown("---")
    meniu = st.sidebar.radio("Mergi la:", 
        ["🏠 LOBBY (MULTIPLAYER)", 
         "🔫 WEAPONS & LOADOUTS", 
         "🎫 BATTLE PASS", 
         "💀 OPERATORS", 
         "🛒 STORE"])
    
    # Afișare User Securizată (folosim .get ca sa nu dea eroare)
    current_user = st.session_state.get('user', 'OPERATOR')
    st.sidebar.markdown("---")
    st.sidebar.success(f"🟢 STATUS: ONLINE\n👤 {current_user.upper()}")
    
    # --- BAZA DE DATE MASIVĂ (ARSENAL COMPLET) ---
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22", "PP-919", "Saug 9mm"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman": ["M8A1", "Warden 308", "M34 Novaline"],
        "Snipers": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI", "HEI-4"],
        "Specials": ["NX Ravager"],
        "Melee": ["Combat Knife", "Baseball Bat"]
    }

    # --- LISTA COMPLETĂ DE ATAȘAMENTE ---
    atasamente = {
        "Optic": ["Iron Sights", "Merlin Mini", "Slate Reflex (+Vis)", "Red Dot (+Acc)", "Kobra Sight", "4x Acog (-Mob)", "Thermal Scope", "Variable Zoom"],
        "Muzzle": ["None", "Suppressor (-Range)", "Compensator (+Acc)", "Muzzle Brake (+Ctrl)", "Flash Guard", "Breacher Device"],
        "Barrel": ["Standard", "Long Barrel (+Range)", "Reinforced Barrel (+Dmg)", "Short Barrel (+Mob)", "Rapid Fire Barrel", "Match Grade"],
        "Underbarrel": ["None", "Vertical Grip (+Ctrl)", "Ranger Foregrip (+Acc)", "Bipod", "Commando Grip", "Laser Sight (+Hip)", "Bruiser Grip"],
        "Magazine": ["Standard Mag", "Fast Mag (+Rld)", "Extended Mag (-Mob)", "Drum Mag (-Mob)", "High Caliber (+Dmg)", "Vandal Mag"],
        "Rear Grip": ["None", "Ergonomic Grip", "Quickdraw Grip (+Hnd)", "Tape Grip", "Stippled Grip", "Field Tape"],
        "Stock": ["Standard", "No Stock (+Mob/-Acc)", "Heavy Stock (+Acc/-Mob)", "Lightweight Stock", "Tactical Stock", "Collapsible Stock"],
        "Fire Mod": ["Standard", "Rapid Fire (+Rate)", "Burst Mod"]
    }

    # ==========================================
    # PAGINA: WEAPONS & GUNSMITH (MAIN)
    # ==========================================
    if meniu == "🔫 WEAPONS & LOADOUTS":
        st.title("🛠️ CREATE A CLASS / GUNSMITH")
        
        # 1. SELECTARE ARMĂ (HOLDER)
        st.markdown("### 1. SELECTARE ARMĂ PRINCIPALĂ")
        col_sel1, col_sel2 = st.columns([1, 2])
        with col_sel1:
            cat_p = st.selectbox("📂 CATEGORIE:", list(arsenal.keys()))
        with col_sel2:
            weapon_p = st.selectbox("🔫 ARMA:", arsenal[cat_p])

        st.markdown("---")

        # 2. GUNSMITH SPLIT-SCREEN REAL
        st.markdown("### 2. GUNSMITH (MODIFICARE LIVE)")
        
        # Împărțim ecranul: Stânga (Piese) - Dreapta (Stats)
        c_parts, c_stats = st.columns([1.5, 1])

        with c_parts:
            st.info(f"Configurare Atașamente pentru: **{weapon_p}**")
            
            # Grid de atașamente (4 rânduri x 2 coloane)
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

        # --- MOTOR MATEMATIC (CALCULE) ---
        # Valori de bază
        fp = 50.0; acc = 50.0; mob = 50.0; hnd = 50.0

        # Bonusuri de clasă (Base Stats)
        if "Sniper" in cat_p: fp=90; acc=80; mob=20; hnd=30
        elif "SMG" in cat_p: fp=40; acc=45; mob=85; hnd=80
        elif "Shotgun" in cat_p: fp=95; acc=25; mob=70; hnd=60
        elif "LMG" in cat_p: fp=70; acc=60; mob=30; hnd=40
        elif "Marksman" in cat_p: fp=75; acc=75; mob=50; hnd=50
        elif "Assault" in cat_p: fp=60; acc=60; mob=60; hnd=60

        # Calcul Impact Atașamente
        # Barrel
        if "Long" in bar: acc += 15; mob -= 10
        if "Short" in bar: mob += 15; acc -= 15
        if "Reinforced" in bar: fp += 10; hnd -= 5
        if "Rapid" in bar: fp += 15; acc -= 10
        # Stock
        if "No Stock" in stk: mob += 20; acc -= 20; hnd -= 10
        if "Heavy" in stk: acc += 15; mob -= 15
        if "Lightweight" in stk: mob += 10; acc -= 5
        # Magazine
        if "Extended" in mag: mob -= 10; hnd -= 5
        if "Fast" in mag: hnd += 10
        if "High Caliber" in mag: fp += 15; hnd -= 10
        # Muzzle
        if "Suppressor" in muz: fp -= 5; hnd += 5
        if "Compensator" in muz: acc += 10; hnd -= 5
        if "Muzzle Brake" in muz: hnd += 5; acc += 5
        # Underbarrel
        if "Vertical" in und: acc += 8; hnd += 2
        if "Ranger" in und: acc += 12; mob -= 5
        if "Laser" in und: hnd += 15; acc -= 5
        # Optic
        if "Zoom" in opt or "Thermal" in opt: mob -= 5; acc += 5
        # Grip
        if "Quickdraw" in grp: hnd += 10
        if "Tape" in grp: acc += 5

        # Normalizare (0-100)
        fp = max(0, min(100, int(fp)))
        acc = max(0, min(100, int(acc)))
        mob = max(0, min(100, int(mob)))
        hnd = max(0, min(100, int(hnd)))

        with c_stats:
            st.markdown(f"### 📊 STATISTICI LIVE")
            st.caption("Valorile se actualizează automat în funcție de piese.")
            
            st.write(f"**🔥 FIREPOWER: {fp}**")
            st.progress(fp/100)
            
            st.write(f"**🎯 ACCURACY: {acc}**")
            st.progress(acc/100)
            
            st.write(f"**🏃 MOBILITY: {mob}**")
            st.progress(mob/100)
            
            st.write(f"**⚡ HANDLING: {hnd}**")
            st.progress(hnd/100)

            st.markdown("---")
            if mob > 80: st.success("🚀 STIL: Run & Gun (Viteză Maximă)")
            elif acc > 80: st.success("🎯 STIL: Long Range Laser (Precizie)")
            elif fp > 85: st.error("💀 STIL: High Damage / One Shot")
            else: st.warning("⚖️ STIL: Balanced / Versatile")
            
            if weapon_p in ["Maddox RFB", "M8A1", "Jäger 45"]:
                st.toast(f"Weapon Mastery Active: {weapon_p}")

        st.markdown("---")
        
        # 3. RESTUL CLASEI (LOADOUT COMPLET)
        st.markdown("### 3. CONFIGURARE RESTUL CLASEI")
        
        c_sec, c_perk, c_wild = st.columns(3)
        with c_sec:
            st.markdown("#### 🔫 SECUNDARĂ & ECHIPAMENT")
            st.selectbox("Arma Secundară", arsenal["Pistols"] + arsenal["Launchers"])
            st.selectbox("Tactical", ["Stim Shot", "Flashbang", "EMP Grenade", "Smoke Grenade", "Shock Charge"])
            st.selectbox("Lethal", ["Frag Grenade", "Semtex", "C4", "Combat Axe", "Drill Charge"])
        
        with c_perk:
            st.markdown("#### 💎 PERKS (SPECIALITĂȚI)")
            st.selectbox("🔵 Perk 1 (Blue)", ["Ghost", "Flak Jacket", "Engineer", "Tac Mask", "Forward Intel"])
            st.selectbox("🟢 Perk 2 (Green)", ["Fast Hands", "Tracker", "Cold Blooded", "Dispatcher", "Quartermaster"])
            st.selectbox("🔴 Perk 3 (Red)", ["Dexterity", "Double Time", "Vigilance", "Gearhead", "Guardian"])

        with c_wild:
            st.markdown("#### 🃏 WILDCARD & UPGRADES")
            st.selectbox("Wildcard", ["Overkill", "Gunfighter", "Perk Greed", "Danger Close"])
            st.selectbox("Field Upgrade", ["Assault Pack", "Trophy System", "Sleeper Agent", "Jammer", "Neurogas"])
            st.selectbox("Scorestreaks", ["UAV / Counter UAV / Hellstorm", "RC-XD / Sniper Heli / VTOL"])

    # ==========================================
    # PAGINA: LOBBY
    # ==========================================
    elif meniu == "🏠 LOBBY (MULTIPLAYER)":
        st.title("MULTIPLAYER LOBBY")
        
        l1, l2 = st.columns([2, 1])
        with l1:
            st.image("https://img.icons8.com/dusk/64/controller.png", width=64)
            st.subheader("FIND A MATCH")
            st.write("Playlist Selectat: **Moshpit (6v6)**")
            st.write("Maps: Nuketown, Raid, Standoff")
            if st.button("START MATCHMAKING", type="primary", use_container_width=True):
                with st.spinner("Searching for lobby..."):
                    time.sleep(2)
                st.success("MATCH FOUND: TDM on Nuketown!")
            
            st.info("⚠️ Daily Challenge: Get 25 Kills with SMGs")
        
        with l2:
            st.markdown("### PLAYER CARD")
            st.warning(f"🔰 {current_user} | Level 55")
            st.progress(1.0, text="Prestige 1 Ready")
            st.write("Friends Online: 4")
            st.write("- Ezgi (Playing Zombies)")
            st.write("- Ghost (In Menu)")

    # ==========================================
    # PAGINA: BATTLE PASS
    # ==========================================
    elif meniu == "🎫 BATTLE PASS":
        st.title("SEZONUL 1: OPERATION BLACK")
        st.write("Sector Activ: **A5**")
        st.progress(0.45, text="Progres Sezon: 45%")
        
        col_bp1, col_bp2 = st.columns(2)
        with col_bp1:
            st.image("https://img.icons8.com/color/96/military-star.png")
            st.button("Claim Tokens (0 Available)")
        with col_bp2:
            st.write("Următorul Reward: **Goliath Operator Skin**")
            st.write("XP Token: 1 Hour Double XP")

    # ==========================================
    # PAGINA: OPERATORS
    # ==========================================
    elif meniu == "💀 OPERATORS":
        st.title("OPERATORS")
        st.write("Faction: **Crimson One**")
        c_op1, c_op2 = st.columns(2)
        with c_op1:
            st.selectbox("Select Operator", ["Hunter", "Song", "Stone", "Powers"])
        with c_op2:
            st.write("Active Skin: **Default**")

    # ==========================================
    # PAGINA: STORE
    # ==========================================
    elif meniu == "🛒 STORE":
        st.title("STORE")
        st.error("Nu cheltui toți banii, șefu'!")
        st.write("Featured Bundle: **Goliath Operator Pack** (2400 CP)")
        st.write("Pro Pack: **Chemical Agent** (19.99$)")

    # ==========================================
    # LOGOUT (JOS DE TOT)
    # ==========================================
    st.sidebar.markdown("---")
    if st.sidebar.button("🔴 DECONECTARE (LOGOUT)"):
        st.session_state.logat = False
        st.session_state.user = ""
        st.rerun()
# ... (restul codului din sidebar) ...
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💰 SUPPORT")
    st.sidebar.info("Îți place aplicația? Mă poți susține cu o cafea!")
    # Aici pui link-ul tau real de PayPal sau Stripe
    st.sidebar.link_button("☕ Cumpără-mi o cafea (Donation)", "https://www.paypal.com")
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🔴 DECONECTARE (LOGOUT)"):
        st.session_state.logat = False
        st.session_state.user = ""
        st.rerun()
