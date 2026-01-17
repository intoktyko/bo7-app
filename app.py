import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith FIXED", page_icon="🛠️", layout="wide")

# --- 1. SISTEM DE LOGIN ---
if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Parola greșită! Încearcă: sefu / admin123")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("CONNECT ONLINE SERVICES", on_click=verifica)

# --- 2. APLICATIA PRINCIPALA ---
else:
    # Sidebar
    st.sidebar.markdown("### ≡ NAVIGARE")
    meniu = st.sidebar.radio("Meniu:", ["🏠 LOBBY", "🔫 WEAPONS & LOADOUTS", "🎫 BATTLE PASS", "🛒 STORE"])

    # --- BAZA DE DATE ARME (ARSENAL) ---
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "AK-27", "MXR-17", "M15 MOD 0", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["Jackal PDW", "C9", "KSV", "Tanto .22", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman": ["M8A1", "Warden 308", "M34 Novaline"],
        "Snipers": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI", "HEI-4"],
        "Specials": ["NX Ravager"]
    }

    # --- BAZA DE DATE
