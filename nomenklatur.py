import tkinter as tk
from tkinter import messagebox, ttk
import random

class ChemieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemie Nomenklatur Trainer")
        self.root.geometry("600x450")
        
        # Datenbasis: Exakt 101 Einträge wie angefordert
        # Format: {"name": str, "formel": str, "falsch": int, "abgefragt": int}
        self.stoffe = [
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
            {"name": "Sulfid-Ion", "formel": "SO32-", "falsch": 0, "abgefragt": 0}, # Anmerkung: Laut Prompt Sulfid, chemisch eher Sulfit
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
        
        # Liste für den aktuellen Durchlauf (wird gemischt)
        self.abfrage_liste = list(self.stoffe)
        self.aktueller_index = 0
        
        self.setup_ui()
        self.starte_neuen_zyklus()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 11))
        
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Fortschrittsanzeige
        self.lbl_progress = ttk.Label(self.main_frame, text="0 / 101")
        self.lbl_progress.pack(pady=(0, 20))
        
        # Frage (Stoffname)
        self.lbl_frage = ttk.Label(self.main_frame, text="", font=("Arial", 16, "bold"), wraplength=500)
        self.lbl_frage.pack(pady=(0, 20))
        
        # Eingabefeld
        self.eingabe_var = tk.StringVar()
        self.entry = ttk.Entry(self.main_frame, textvariable=self.eingabe_var, font=("Arial", 14))
        self.entry.pack(pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.pruefen())
        
        # Rückmeldung
        self.lbl_feedback = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.lbl_feedback.pack(pady=(0, 20))
        
        # Buttons
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        self.btn_pruefen = ttk.Button(btn_frame, text="Prüfen", command=self.pruefen)
        self.btn_pruefen.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.btn_next = ttk.Button(btn_frame, text="Nächste", command=self.naechste_frage, state=tk.DISABLED)
        self.btn_next.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Untere Leiste
        bottom_frame = ttk.Frame(self.main_frame)
        bottom_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(bottom_frame, text="Neuer Zyklus", command=self.starte_neuen_zyklus).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="Statistik anzeigen", command=self.zeige_statistik).pack(side=tk.RIGHT, padx=5)

    def normalisiere_eingabe(self, text):
        # Leerzeichen entfernen
        text = text.replace(" ", "")
        
        # Tiefgestellte Zahlen in normale Zahlen umwandeln
        subs = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
        text = text.translate(subs)
        
        # Ggf. weitere Zeichen normalisieren (Hochgestellte Zahlen/Zeichen)
        supers = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+-")
        text = text.translate(supers)
        
        # Minus-Zeichen vereinheitlichen (Unicode Minus, Hyphen, En-dash, Em-dash)
        text = text.replace("−", "-").replace("–", "-").replace("—", "-")
        
        return text

    def starte_neuen_zyklus(self):
        random.shuffle(self.abfrage_liste)
        self.aktueller_index = 0
        self.entry.delete(0, tk.END)
        self.lbl_feedback.config(text="", foreground="black")
        self.btn_pruefen.config(state=tk.NORMAL)
        self.btn_next.config(state=tk.DISABLED)
        self.update_frage()

    def update_frage(self):
        if self.aktueller_index < len(self.abfrage_liste):
            stoff = self.abfrage_liste[self.aktueller_index]
            self.lbl_frage.config(text=stoff["name"])
            self.lbl_progress.config(text=f"{self.aktueller_index + 1} / {len(self.abfrage_liste)}")
            self.entry.delete(0, tk.END)
            self.entry.focus()
            self.lbl_feedback.config(text="", foreground="black")
            self.btn_pruefen.config(state=tk.NORMAL)
            self.btn_next.config(state=tk.DISABLED)
            
            # Reset entry bind to Pruefen
            self.entry.bind("<Return>", lambda event: self.pruefen())
        else:
            self.zeige_statistik_popup()

    def pruefen(self):
        if self.aktueller_index >= len(self.abfrage_liste):
            return

        eingabe = self.eingabe_var.get()
        norm_eingabe = self.normalisiere_eingabe(eingabe)
        
        aktueller_stoff = self.abfrage_liste[self.aktueller_index]
        korrekt = self.normalisiere_eingabe(aktueller_stoff["formel"])
        
        aktueller_stoff["abgefragt"] += 1
        
        if norm_eingabe == korrekt:
            self.lbl_feedback.config(text=f"✅ Richtig! ({aktueller_stoff['formel']})", foreground="green")
        else:
            aktueller_stoff["falsch"] += 1
            self.lbl_feedback.config(text=f"❌ Falsch! Richtige Antwort: {aktueller_stoff['formel']}", foreground="red")
            
        self.btn_pruefen.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)
        self.entry.bind("<Return>", lambda event: self.naechste_frage()) 
        self.btn_next.focus()

    def naechste_frage(self):
        self.aktueller_index += 1
        self.update_frage()

    def zeige_statistik_popup(self):
        self.zeige_statistik(end_of_cycle=True)
        # Optional: Nach dem Popup fragen, ob ein neuer Zyklus gestartet werden soll?
        # messagebox ist modal, das reicht erst mal.

    def zeige_statistik(self, end_of_cycle=False):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistik")
        stats_window.geometry("500x600")
        
        container = ttk.Frame(stats_window)
        container.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Gruppieren nach Fehleranzahl
        fehler_gruppen = {}
        for stoff in self.stoffe:
            f = stoff["falsch"]
            if f > 0:
                if f not in fehler_gruppen:
                    fehler_gruppen[f] = []
                fehler_gruppen[f].append(stoff)
        
        if not fehler_gruppen:
            msg = "Keine falschen Antworten – sehr gut!" if end_of_cycle else "Bisher keine Fehler."
            ttk.Label(scrollable_frame, text=msg, font=("Arial", 12, "bold"), foreground="green").pack(pady=20, padx=20)
        else:
            sorted_keys = sorted(fehler_gruppen.keys())
            for anz in sorted_keys:
                gruppe = fehler_gruppen[anz]
                
                header_text = f"{anz}× falsch:"
                ttl = ttk.Label(scrollable_frame, text=header_text, font=("Arial", 12, "bold", "underline"))
                ttl.pack(anchor="w", pady=(15, 5), padx=10)
                
                for stoff in gruppe:
                    txt = f"- {stoff['name']} → {stoff['formel']}"
                    ttk.Label(scrollable_frame, text=txt, font=("Arial", 11)).pack(anchor="w", padx=20)

        # Wenn Pflichtauswertung am Ende, Button zum Schließen + Neuer Zyklus in Hauptfenster
        btn_close = ttk.Button(stats_window, text="Schließen", command=stats_window.destroy)
        btn_close.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChemieApp(root)
    root.mainloop()
