import streamlit as st

st.set_page_config(page_title="BO7 Gunsmith PRO", page_icon="📊", layout="wide")

if 'logat' not in st.session_state:
    st.session_state.logat = False

def verifica():
    if st.session_state.user.lower() == "sefu" and st.session_state.parola == "admin123":
        st.session_state.logat = True
    else:
        st.error("Date incorecte!")

if not st.session_state.logat:
    st.title("🔒 BO7 War Room Login")
    st.text_input("Utilizator:", key="user")
    st.text_input("Parola:", type="password", key="parola")
    st.button("Intră în Armurărie", on_click=verifica)
else:
    st.sidebar.title("🎮 Meniu Armurier")
    # Arsenalul tău (cele 9 categorii)
    arsenal = {
        "Assault Rifles": ["Maddox RFB", "M15 MOD 0", "AK-27", "MXR-17", "X9 Maverick", "DS20 Mirage", "Peacekeeper MK1"],
        "SMGs": ["C9", "KSV", "Tanto .22", "Jackal PDW", "PP-919"],
        "Shotguns": ["M10 Breacher", "ASG-89"],
        "LMGs": ["Sokol 545", "MK.7B", "XM325"],
        "Marksman Rifles": ["M8A1", "Warden 308", "M34 Novaline"],
        "Sniper Rifles": ["VS Recon", "Hawker HX", "Shadow SK", "XR-3 ION"],
        "Pistols": ["Jäger 45", "Velox 8.7", "Coda 9"],
        "Launchers": ["AAROW 109", "A.R.C. MI"],
        "Specials": ["NX Ravager"]
    }

    st.header("🔧 Gunsmith Simulator")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        cat = st.selectbox("Categorie:", list(arsenal.keys()))
        arma = st.selectbox("Arma:", arsenal[cat])
        st.write("---")
        # Selectori Atasamente
        opt = st.selectbox("Optic:", ["Standard", "Slate Reflex", "Red Dot", "4x Optic"])
        muz = st.selectbox("Muzzle:", ["None", "Suppressor", "Compensator"])
        bar = st.selectbox("Barrel:", ["Standard", "Long Barrel (+Range)", "Short Barrel (+Speed)"])
        und = st.selectbox("Underbarrel:", ["None", "Vertical Grip (+Control)", "Ranger Foregrip"])
        mag = st.selectbox("Magazine:", ["Standard", "Fast Mag", "Extended Mag"])

    with col2:
        st.subheader(f"📊 Statistici Live: {arma}")
        
        # Logica de calcul statistici (Simulare)
        firepower = 60
        accuracy = 55
        mobility = 50
        handling = 45

        # Modificari in functie de selectie
        if "Long Barrel" in bar: accuracy += 15; mobility -= 10
        if "Short Barrel" in bar: mobility += 15; accuracy -= 10
        if "Vertical Grip" in und: accuracy += 10; handling += 5
        if "Suppressor" in muz: handling += 10; firepower -= 5
        if "Fast Mag" in mag: handling += 15; mobility -= 5

        # Afisare Bare (ca in joc)
        st.write(f"🔥 Firepower: {firepower}")
        st.progress(min(firepower/100, 1.0))
        
        st.write(f"🎯 Accuracy: {accuracy}")
        st.progress(min(accuracy/100, 1.0))
        
        st.write(f"🏃 Mobility: {mobility}")
        st.progress(min(mobility/100, 1.0))
        
        st.write(f"⚡ Handling: {handling}")
        st.progress(min(handling/100, 1.0))

        st.write("---")
        if arma in ["Maddox RFB", "M8A1", "VS Recon", "Jäger 45"]:
            st.success("⭐ STATUS: NIVEL MAXIM ATINS")
            st.write("Toate atașamentele sunt deblocate pentru testare.")

    if st.sidebar.button("Logout"):
        st.session_state.logat = False
        st.rerun()
