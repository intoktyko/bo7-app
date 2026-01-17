import streamlit as st

st.set_page_config(page_title="BO7 Ultimate Loadout", page_icon="🔫", layout="wide")

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
    # MENIU STÂNGA (NAVIGARE)
    st.sidebar.markdown("### ≡ NAVIGARE JOC")
    meniu = st.sidebar.radio("Mergi la:", ["🏠 LOBBY", "🔫 WEAPONS & LOADOUTS", "🎫 BATTLE PASS", "🛒 STORE"])

    # --- BAZA DE DATE COMPLETA (Actualizată cu tot ce ai cerut) ---
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

    # TOATE ATAȘAMENTELE POSIBILE
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

    # --- PAGINA: WEAPONS & LOADOUTS ---
    if meniu == "🔫 WEAPONS & LOADOUTS":
        st.title("CREATE A CLASS")
        
        # Tabs: Loadout (General) vs Gunsmith (Detaliat)
        tab1, tab2 = st.tabs(["📂 LOADOUT PRINCIPAL", "🔧 GUNSMITH (ARMURIER)"])

        # --- TAB 1: LOADOUT OVERVIEW ---
        with tab1:
            st.subheader("CUSTOM CLASS 1")
            
            # PRIMARY & WILDCARD
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown("### 🔫 PRIMARY WEAPON")
                cat_p = st.selectbox("Categorie:", list(arsenal.keys())[:-1], key="cat_p") # Fara Melee
                weapon_p = st.selectbox("Arma:", arsenal[cat_p], key="weapon_p")
                st.info(f"Selectat: **{weapon_p}**")
            with c2:
                st.markdown("### 🃏 WILDCARD")
                st.selectbox("Card:", ["Overkill", "Gunfighter", "Perk Greed", "Danger Close"])

            st.markdown("---")

            # SECONDARY & MELEE
            c3, c4 = st.columns(2)
            with c3:
                st.markdown("### 🔫 SECONDARY")
                st.selectbox("Arma Secundara:", arsenal["Pistols"] + arsenal["Launchers"])
            with c4:
                st.markdown("### 🔪 MELEE")
                st.selectbox("Arma Alba:", arsenal["Melee"])

            st.markdown("---")

            # EQUIPMENT & FIELD UPGRADE
            eq1, eq2, eq3 = st.columns(3)
            with eq1: st.selectbox("TACTICAL", ["Stim Shot", "Flashbang", "EMP Grenade", "Smoke"])
            with eq2: st.selectbox("LETHAL", ["Frag Grenade", "Semtex", "C4", "Combat Axe"])
            with eq3: st.selectbox("FIELD UPGRADE", ["Assault Pack", "Trophy System", "Sleeper Agent"])

            # PERKS
            st.markdown("### 💎 PERKS")
            pk1, pk2, pk3 = st.columns(3)
            with pk1: st.selectbox("🔵 PERK 1", ["Ghost", "Flak Jacket", "Engineer", "Gung-Ho"])
            with pk2: st.selectbox("🟢 PERK 2", ["Fast Hands", "Tracker", "Cold Blooded", "Dispatcher"])
            with pk3: st.selectbox("🔴 PERK 3", ["Dexterity", "Double Time", "Vigilance", "Quartermaster"])

        # --- TAB 2: GUNSMITH (CONSTRUIESTE ARMA) ---
        with tab2:
            st.header(f"🔧 GUNSMITH: {weapon_p}")
            st.caption("Alege cele 8 atașamente permise:")

            col_parts, col_stats = st.columns([2, 1])
            
            with col_parts:
                # 8 SLOTURI COMPLETE
                r1_a, r1_b = st.columns(2)
                with r1_a: st.selectbox("👁️ OPTIC", atasamente["Optic"])
                with r1_b: st.selectbox("🔇 MUZZLE", atasamente["Muzzle"])
                
                r2_a, r2_b = st.columns(2)
                with r2_a: st.selectbox("📏 BARREL", atasamente["Barrel"])
                with r2_b: st.selectbox("✊ UNDERBARREL", atasamente["Underbarrel"])
                
                r3_a, r3_b = st.columns(2)
                with r3_a: st.selectbox("🔋 MAGAZINE", atasamente["Magazine"])
                with r3_b: st.selectbox("🧤 REAR GRIP", atasamente["Rear Grip"])
                
                r4_a, r4_b = st.columns(2)
                with r4_a: st.selectbox("🍑 STOCK", atasamente["Stock"])
                with r4_b: st.selectbox("🔥 FIRE MOD", atasamente["Fire Mod"])

            with col_stats:
                st.markdown("### 📊 STATISTICI LIVE")
                # Valori simulate (ca sa se miste barele cand schimbi)
                fp = 55; acc = 60; mob = 65; hnd = 50
                
                # Simulăm impactul atașamentelor
                if "Sniper" in cat_p: fp += 30; mob -= 30
                if "SMG" in cat_p: mob += 20; acc -= 10
                
                st.write("🔥 Firepower"); st.progress(min(fp/100, 1.0))
                st.write("🎯 Accuracy"); st.progress(min(acc/100, 1.0))
                st.write("🏃 Mobility"); st.progress(min(mob/100, 1.0))
                st.write("⚡ Handling"); st.progress(min(hnd/100, 1.0))
                
                if weapon_p in ["Maddox RFB", "M8A1"]:
                    st.success("🏆 MASTER BADGE: GOLD")

    # --- RESTUL MENIURILOR ---
    elif meniu == "🏠 LOBBY":
        st.title("MULTIPLAYER LOBBY")
        st.button("FIND A MATCH", type="primary")
    
    elif meniu == "🎫 BATTLE PASS":
        st.title("BATTLE PASS")
        st.write("Season 1: Active")

    elif meniu == "🛒 STORE":
        st.title("STORE")
        st.write("No new bundles.")

    # BUTON LOGOUT
    st.sidebar.markdown("---")
    if st.sidebar.button("Ieșire (Logout)"):
        st.session_state.logat = False
        st.rerun()
