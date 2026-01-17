import streamlit as st

st.set_page_config(page_title="BO7 ULTIMATE COMPANION", page_icon="💀", layout="wide")

# ==========================================
# 1. SISTEM DE SECURITATE (LOGIN)
# ==========================================
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica_parola():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("❌ Acces Respins! Date incorecte.")

if not st.session_state.logat:
    st.markdown("<h1 style='text-align: center;'>🔒 BO7 WAR ROOM</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.text_input("Operativ:", key="user")
        st.text_input("Cod Acces:", type="password", key="parola")
        st.button("INIȚIALIZARE SISTEM", on_click=verifica_parola, type="primary", use_container_width=True)

# ==========================================
# 2. INTERFAȚA PRINCIPALĂ (DUPĂ LOGIN)
# ==========================================
else:
    # --- MENIU LATERAL (NAVIGARE) ---
    st.sidebar.markdown("## ≡ NAVIGARE TACTICĂ")
    meniu = st.sidebar.radio("Mergi la:", 
        ["🏠 LOBBY", "🔫 WEAPONS (LOADOUTS)", "🎫 BATTLE PASS", "💀 OPERATORS", "🛒 STORE"])
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"🟢 Status: ONLINE\n👤 User: {st.session_state.user.upper()}")

    # --- BAZA DE DATE MASIVĂ (ARSENAL) ---
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

    # --- BAZA DE DATE ATAȘAMENTE (DETALIATĂ) ---
    atasamente = {
        "Optic": ["Iron Sights", "Merlin Mini", "Slate Reflex (+Vis)", "Red Dot (+Acc)", "Kobra Sight", "4x Acog (-Mob)", "Thermal Scope", "Variable Zoom"],
        "Muzzle": ["None", "Suppressor (-Range)", "Compensator (+Acc)", "Muzzle Brake (+Ctrl)", "Flash Guard"],
        "Barrel": ["Standard", "Long Barrel (+Range)", "Reinforced Barrel (+Dmg)", "Short Barrel (+Mob)", "Rapid Fire Barrel"],
        "Underbarrel": ["None", "Vertical Grip (+Ctrl)", "Ranger Foregrip (+Acc)", "Bipod", "Commando Grip", "Laser Sight (+Hip)"],
        "Magazine": ["Standard Mag", "Fast Mag (+Rld)", "Extended Mag (-Mob)", "Drum Mag (-Mob)", "High Caliber (+Dmg)"],
        "Rear Grip": ["None
