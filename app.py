import streamlit as st

st.set_page_config(page_title="BO7 Main Menu", page_icon="🎮", layout="wide")

# --- LOGIN ---
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Acces Respins!")

if not st.session_state.logat:
    st.title("🔒 BO7 Companion Login")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("CONNECT ONLINE SERVICES", on_click=verifica)

# --- MENIUL JOCULUI (Dupa logare) ---
else:
    # 1. BARA DE SUS (Navigare ca in joc)
    st.sidebar.markdown("### ≡ NAVIGARE RAPIDĂ")
    meniu_principal = st.sidebar.radio("Selectează Meniul:", 
        ["🏠 LOBBY", "🔫 WEAPONS", "🎫 BATTLE PASS", "💀 OPERATORS", "🛒 STORE"])

    # --- TAB: LOBBY ---
    if meniu_principal == "🏠 LOBBY":
        st.title("MULTIPLAYER LOBBY")
        
        # Simulare ecran Lobby
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### FIND A MATCH")
            st.write("Current Playlist: **Moshpit (6v6)**")
            st.button("START MATCHMAKING", type="primary", use_container_width=True)
            
            st.write("---")
            st.info("⚠️ **Daily Message:** Double XP Weekend is ACTIVE!")
            
        with col2:
            st.markdown("### PLAYER CARD")
            st.warning(f"🔰 {st.session_state.user} | Level 55 (Prestige 1)")
            st.write("Online Friends: 3")

    # --- TAB: WEAPONS (Aici e grosul) ---
    elif meniu_principal == "🔫 WEAPONS":
        # Sub-meniu specific armelor
        tab1, tab2, tab3 = st.tabs(["📂 LOADOUTS (CLASE)", "🔧 GUNSMITH (ARMURIER)", "🎨 CAMOS (SKINURI)"])

        # SUB-TAB 1: LOADOUTS (Ca in poza 1000050632.jpg)
        with tab1:
            st.subheader("EDIT LOADOUT")
            c1, c2 = st.columns([3, 1])
            with c1:
                st.success("🔫 PRIMARY: Maddox RFB")
                st.info("🔫 SECONDARY: Jäger 45")
                st.error("🔪 MELEE: Knife")
            with c2:
                st.warning("🃏 WILDCARD: Overkill")
            
            st.write("---")
            k1, k2, k3 = st.columns(3)
            with k1: st.selectbox("TACTICAL", ["EMP Grenade", "Stim", "Flash"])
            with k2: st.selectbox("LETHAL", ["Frag", "Semtex", "C4"])
            with k3: st.selectbox("FIELD UPGRADE", ["Drone Pod", "Trophy System"])
            
            p1, p2, p3 = st.columns(3)
            with p1: st.write("🔵 **Perk 1:** Gearhead")
            with p2: st.write("🟢 **Perk 2:** Vigilance")
            with p3: st.write("🔴 **Perk 3:** Dexterity")

        # SUB-TAB 2: GUNSMITH (Simulatorul tau preferat)
        with tab2:
            st.subheader("🔧 ARMURIER (Statistici Live)")
            
            arsenal = {
                "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17"],
                "SMGs": ["Jackal PDW", "C9", "KSV"],
                "Marksman": ["M8A1", "Warden 308"],
                "Snipers": ["VS Recon", "Hawker HX"],
                "LMGs": ["Sokol 545", "MK.7B"],
                "Shotguns": ["M10 Breacher"],
                "Pistols": ["Jäger 45"],
                "Specials": ["NX Ravager", "AAROW 109"]
            }
            
            col_a, col_b = st.columns(2)
            with col_a:
                cat = st.selectbox("Categorie:", list(arsenal.keys()))
                arma = st.selectbox("Arma:", arsenal[cat])
                
                st.markdown("**Atașamente:**")
                # Selectori simplificati pentru demo
                st.selectbox("Optic", ["Red Dot", "4x Scope", "Thermal"])
                st.selectbox("Barrel", ["Long Barrel", "Short Barrel"])
                st.selectbox("Underbarrel", ["Vertical Grip", "Ranger Grip"])
            
            with col_b:
                st.markdown(f"### 📊 Stats: {arma}")
                # Bare statice deocamdata, le facem mobile dupa ce confirmi structura
                st.write("Firepower"); st.progress(0.7)
                st.write("Accuracy"); st.progress(0.6)
                st.write("Mobility"); st.progress(0.5)

        # SUB-TAB 3: CAMOS (Tracker)
        with tab3:
            st.subheader("🎨 PROGRES CAMUFLAJE")
            st.image("https://img.icons8.com/color/48/military-backpack.png", width=50) # Placeholder icon
            st.write("Bifează ce ai deblocat (Ca în meniul Mastery):")
            c_a, c_b = st.columns(2)
            with c_a:
                st.checkbox("GOLD Camo")
                st.checkbox("DIAMOND Camo")
            with c_b:
                st.checkbox("DARK MATTER")
                st.checkbox("ELEVATE (Universal)")

    # --- TAB: BATTLE PASS ---
    elif meniu_principal == "🎫 BATTLE PASS":
        st.title("SEZONUL 1: BATTLE PASS")
        # Simulare Token Bank
        st.info("💎 TOKEN BANK: 0 Tokens Available")
        st.progress(0.35, text="Progres Sezon: 35%")
        st.write("Reward Următor: Skin Operator 'Goliath'")

    # --- ALTELE ---
    elif meniu_principal == "💀 OPERATORS":
        st.title("OPERATORS")
        st.write("Selectează personajul tău (West vs East).")
    
    elif meniu_principal == "🛒 STORE":
        st.title("STORE")
        st.warning("Nu cheltui toți banii, șefu'!")

    # Buton Logout jos in sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logat = False
        st.rerun()
