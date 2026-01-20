import streamlit as st
import random

# --- 1. DATENBASIS ---
if 'stoffe' not in st.session_state:
    st.session_state.stoffe = [
        {"name": "Aluminiumchlorid", "formel": "AlCl3", "falsch": 0, "abgefragt": 0},
        {"name": "Aluminiumphosphat", "formel": "AlPO4", "falsch": 0, "abgefragt": 0},
        {"name": "Ameisensäure", "formel": "HCOOH", "falsch": 0, "abgefragt": 0},
        {"name": "Ammoniak", "formel": "NH3", "falsch": 0, "abgefragt": 0},
        {"name": "Ammonium", "formel": "NH4+", "falsch": 0, "abgefragt": 0},
        {"name": "Ammoniumhydroxid", "formel": "NH4OH", "falsch": 0, "abgefragt": 0},
        {"name": "Arsentrioxid", "formel": "As2O3", "falsch": 0, "abgefragt": 0},
        {"name": "Bariumcarbid", "formel": "BaC2", "falsch": 0, "abgefragt": 0},
        {"name": "Bariumcarbonat", "formel": "BaCO3", "falsch": 0, "abgefragt": 0},
        {"name": "Bariumfluorid", "formel": "BaF2", "falsch": 0, "abgefragt": 0},
        {"name": "Bariumnitrat", "formel": "Ba(NO3)2", "falsch": 0, "abgefragt": 0},
        {"name": "Bariumsulfid", "formel": "BaS", "falsch": 0, "abgefragt": 0},
        {"name": "Berylliumcarbonat", "formel": "BeCO3", "falsch": 0, "abgefragt": 0},
        {"name": "Bismut(III)hydroxid", "formel": "Bi(OH)3", "falsch": 0, "abgefragt": 0},
        {"name": "Blei(II)sulfid", "formel": "PbS", "falsch": 0, "abgefragt": 0},
        {"name": "Bleisulfat", "formel": "PbSO4", "falsch": 0, "abgefragt": 0},
        {"name": "Cadmiumchlorid", "formel": "CdCl2", "falsch": 0, "abgefragt": 0},
        {"name": "Cadmiumtetrachlorid", "formel": "Cd3Cl4", "falsch": 0, "abgefragt": 0},
        {"name": "Cadmiumtrioxid", "formel": "CdO3", "falsch": 0, "abgefragt": 0},
        {"name": "Calciumcarbonat", "formel": "CaCO3", "falsch": 0, "abgefragt": 0},
        {"name": "Calciumhydroxid", "formel": "Ca(OH)2", "falsch": 0, "abgefragt": 0},
        {"name": "Carbonat-Ion", "formel": "CO32-", "falsch": 0, "abgefragt": 0},
        {"name": "Chlor", "formel": "Cl", "falsch": 0, "abgefragt": 0},
        {"name": "Chrom(III)oxid", "formel": "Cr2O3", "falsch": 0, "abgefragt": 0},
        {"name": "Distickstoffmonoxid", "formel": "N2O", "falsch": 0, "abgefragt": 0},
        {"name": "Eisen(II)oxid", "formel": "FeO", "falsch": 0, "abgefragt": 0},
        {"name": "Eisen(III)oxid", "formel": "Fe2O3", "falsch": 0, "abgefragt": 0},
        {"name": "Eisen(II,III)oxid", "formel": "Fe3O4", "falsch": 0, "abgefragt": 0},
        {"name": "Eisendioxid", "formel": "FeO2", "falsch": 0, "abgefragt": 0},
        {"name": "Eisentrifluorid", "formel": "FeF3", "falsch": 0, "abgefragt": 0},
        {"name": "Essigsäure", "formel": "CH3COOH", "falsch": 0, "abgefragt": 0},
        {"name": "Flusssäure (Fluorwasserstoff)", "formel": "HF", "falsch": 0, "abgefragt": 0},
        {"name": "Formiat-Ion", "formel": "HCOO-", "falsch": 0, "abgefragt": 0},
        {"name": "Glucose", "formel": "C6H12O6", "falsch": 0, "abgefragt": 0},
        {"name": "Hydroxid", "formel": "OH-", "falsch": 0, "abgefragt": 0},
        {"name": "Iodwasserstoff", "formel": "H2I", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumcarbonat", "formel": "K2CO3", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumfluorid", "formel": "KF", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumhydroxid", "formel": "KOH", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumiodid", "formel": "KI", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumnitrat", "formel": "KNO3", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumnitrit", "formel": "KNO2", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumpermanganat", "formel": "KMnO4", "falsch": 0, "abgefragt": 0},
        {"name": "Kaliumsulfat", "formel": "K2SO4", "falsch": 0, "abgefragt": 0},
        {"name": "Kalziumphosphat", "formel": "Ca3(PO4)2", "falsch": 0, "abgefragt": 0},
        {"name": "Kalziumsulfat", "formel": "CaSO4", "falsch": 0, "abgefragt": 0},
        {"name": "Kohlendioxid", "formel": "CO2", "falsch": 0, "abgefragt": 0},
        {"name": "Kohlenmonoxid", "formel": "CO", "falsch": 0, "abgefragt": 0},
        {"name": "Kohlensäure", "formel": "H2CO3", "falsch": 0, "abgefragt": 0},
        {"name": "Kupfersulfat", "formel": "CuSO4", "falsch": 0, "abgefragt": 0},
        {"name": "Magnesiumacetat", "formel": "(CH3COO)2", "falsch": 0, "abgefragt": 0},
        {"name": "Magnesiumchlorid", "formel": "MgCl2", "falsch": 0, "abgefragt": 0},
        {"name": "Magnesiumhydroxid", "formel": "Mg(OH)2", "falsch": 0, "abgefragt": 0},
        {"name": "Magnesiumnitrat", "formel": "Mg(NO3)2", "falsch": 0, "abgefragt": 0},
        {"name": "Mangan(IV)oxid", "formel": "MnO2", "falsch": 0, "abgefragt": 0},
        {"name": "Mangandichlorid", "formel": "MnCl2", "falsch": 0, "abgefragt": 0},
        {"name": "Methan", "formel": "CH4", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumchlorid", "formel": "NaCl", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumdihydrogenphosphat", "formel": "NaH2PO4", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumhexahydroxoaluminat(III)", "formel": "Na3Al(OH)6", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumsulfat", "formel": "Na2SO4", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumsulfid", "formel": "Na2S", "falsch": 0, "abgefragt": 0},
        {"name": "Natriumsulfit", "formel": "Na2SO3", "falsch": 0, "abgefragt": 0},
        {"name": "Natronlauge / Natriumhydroxid", "formel": "NaOH", "falsch": 0, "abgefragt": 0},
        {"name": "Nickel(II)hydroxid", "formel": "Ni(OH)2", "falsch": 0, "abgefragt": 0},
        {"name": "Nitrat-Ion", "formel": "NO3-", "falsch": 0, "abgefragt": 0},
        {"name": "Osmiumdioxid", "formel": "OsO2", "falsch": 0, "abgefragt": 0},
        {"name": "Pentafluoridphosphor", "formel": "PF5", "falsch": 0, "abgefragt": 0},
        {"name": "Perchlorat", "formel": "ClO4-", "falsch": 0, "abgefragt": 0},
        {"name": "Perchlorsäure", "formel": "HClO4", "falsch": 0, "abgefragt": 0},
        {"name": "Phosphat-Ion", "formel": "PO43-", "falsch": 0, "abgefragt": 0},
        {"name": "Phosphin", "formel": "PH3", "falsch": 0, "abgefragt": 0},
        {"name": "Phosphorsäure", "formel": "H3PO4", "falsch": 0, "abgefragt": 0},
        {"name": "Salpetersäure", "formel": "HNO3", "falsch": 0, "abgefragt": 0},
        {"name": "Salpetrige Säure", "formel": "HNO2", "falsch": 0, "abgefragt": 0},
        {"name": "Salzsäure (Wasserstoffchlorid)", "formel": "HCl", "falsch": 0, "abgefragt": 0},
        {"name": "Schwefeldioxid", "formel": "SO2", "falsch": 0, "abgefragt": 0},
        {"name": "Schwefelsäure", "formel": "H2SO4", "falsch": 0, "abgefragt": 0},
        {"name": "Schwefelwasserstoff", "formel": "H2S", "falsch": 0, "abgefragt": 0},
        {"name": "Schweflige Säure", "formel": "H2SO3", "falsch": 0, "abgefragt": 0},
        {"name": "Selendioxid", "formel": "SeO2", "falsch": 0, "abgefragt": 0},
        {"name": "Silberchlorid", "formel": "AgCl", "falsch": 0, "abgefragt": 0},
        {"name": "Siliciumtetrachlorid", "formel": "SiCl4", "falsch": 0, "abgefragt": 0},
        {"name": "Siliziumdioxid", "formel": "SiO2", "falsch": 0, "abgefragt": 0},
        {"name": "Stickstoffdioxid", "formel": "NO2", "falsch": 0, "abgefragt": 0},
        {"name": "Stickstoffmonoxid", "formel": "NO", "falsch": 0, "abgefragt": 0},
        {"name": "Strontiumsulfat", "formel": "SrSO4", "falsch": 0, "abgefragt": 0},
        {"name": "Sulfat-Ion", "formel": "SO42-", "falsch": 0, "abgefragt": 0},
        {"name": "Sulfid-Ion", "formel": "SO32-", "falsch": 0, "abgefragt": 0},
        {"name": "Sulfid-Ion", "formel": "S2-", "falsch": 0, "abgefragt": 0},
        {"name": "Titan(III)chlorid", "formel": "TiCl3", "falsch": 0, "abgefragt": 0},
        {"name": "Titan(IV)chlorid", "formel": "TiCl4", "falsch": 0, "abgefragt": 0},
        {"name": "Titandioxid", "formel": "TiO2", "falsch": 0, "abgefragt": 0},
        {"name": "Uran(V)oxid", "formel": "U2O5", "falsch": 0, "abgefragt": 0},
        {"name": "Wasser", "formel": "H2O", "falsch": 0, "abgefragt": 0},
        {"name": "Wasserstoffbromid", "formel": "HBr", "falsch": 0, "abgefragt": 0},
        {"name": "Wasserstoffiodid", "formel": "HI", "falsch": 0, "abgefragt": 0},
        {"name": "Wasserstoffion", "formel": "H+", "falsch": 0, "abgefragt": 0},
        {"name": "Wasserstoffperoxid", "formel": "H2O2", "falsch": 0, "abgefragt": 0},
        {"name": "Zinksulfid", "formel": "ZnS", "falsch": 0, "abgefragt": 0},
        {"name": "Zinntetrachlorid", "formel": "SnCl4", "falsch": 0, "abgefragt": 0},
    ]

# --- 2. HILFSFUNKTIONEN ---
def normalisiere_eingabe(text):
    text = text.replace(" ", "")
    subs = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    text = text.translate(subs)
    supers = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+-")
    text = text.translate(supers)
    text = text.replace("−", "-").replace("–", "-").replace("—", "-")
    return text

def start_new_cycle():
    st.session_state.abfrage_liste = list(st.session_state.stoffe)
    random.shuffle(st.session_state.abfrage_liste)
    st.session_state.index = 0
    st.session_state.feedback = None
    st.session_state.finished = False

# --- 3. SESSION STATE INITIALISIERUNG ---
if 'index' not in st.session_state:
    start_new_cycle()

# --- 4. UI (DAS AUSSEHEN) ---
st.title("🧪 Chemie Nomenklatur Trainer")

if not st.session_state.finished:
    # Fortschritt
    total = len(st.session_state.abfrage_liste)
    current = st.session_state.index
    progress = current / total
    st.progress(progress)
    st.write(f"Frage {current + 1} von {total}")

    # Aktueller Stoff
    current_stoff = st.session_state.abfrage_liste[current]
    st.header(current_stoff["name"])

    # Eingabeformular
    with st.form(key='answer_form', clear_on_submit=True):
        user_input = st.text_input("Formel eingeben:", key="input_field")
        submit_button = st.form_submit_button(label='Prüfen')

    # Logik beim Klicken
    if submit_button:
        norm_input = normalisiere_eingabe(user_input)
        korrekt = normalisiere_eingabe(current_stoff["formel"])

        if norm_input == korrekt:
            st.success(f"Richtig! {current_stoff['formel']}")
            st.session_state.feedback = "correct"
            current_stoff["abgefragt"] += 1
        else:
            # Finde den originalen Stoff im Hauptspeicher und erhöhe Fehlerzähler
            for s in st.session_state.stoffe:
                if s["name"] == current_stoff["name"]:
                    s["falsch"] += 1
                    s["abgefragt"] += 1
            st.error(f"Falsch! Richtige Antwort: {current_stoff['formel']}")
            st.session_state.feedback = "wrong"
        
        # Zum nächsten springen (Session State Logik)
        st.session_state.index += 1
        if st.session_state.index >= len(st.session_state.abfrage_liste):
            st.session_state.finished = True
        else:
            # Automatischer Rerun, um die nächste Frage anzuzeigen
            # Da wir clear_on_submit verwendet haben, ist das Eingabefeld leer
            st.rerun()

    # Falls wir im nächsten Render-Zyklus noch die Antwort anzeigen wollen, ist das bei Streamlit tricky, 
    # da st.rerun() sofort das UI neu zeichnet.
    # Bei dieser einfachen Implementierung sieht man das Feedback nur kurz, wenn man nicht rerunnt,
    # aber wenn man rerunnt, ist das Feedback weg.
    # Besserer Ansatz: State für "Answer Reviewed"
    
else:
    # --- STATISTIK AM ENDE ---
    st.success("Zyklus beendet!")
    
    fehler_gefunden = False
    
    # Gruppierung
    fehler_gruppen = {}
    for stoff in st.session_state.stoffe:
        f = stoff["falsch"]
        if f > 0:
            fehler_gefunden = True
            if f not in fehler_gruppen:
                fehler_gruppen[f] = []
            fehler_gruppen[f].append(stoff)
    
    if not fehler_gefunden:
        st.balloons()
        st.write("Perfekt! Keine Fehler.")
    else:
        st.write("### Deine Fehlerstatistik:")
        sorted_keys = sorted(fehler_gruppen.keys())
        for anz in sorted_keys:
            st.subheader(f"{anz}x falsch beantwortet:")
            for s in fehler_gruppen[anz]:
                st.write(f"- **{s['name']}** → {s['formel']}")

    if st.button("Neuen Zyklus starten"):
        start_new_cycle()
        st.rerun()
