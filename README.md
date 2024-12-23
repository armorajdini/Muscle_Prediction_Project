# Muskel- und Fettmasse Vorhersage mit maschinellem Lernen

## Projektbeschreibung
Dieses Projekt verwendet ein maschinelles Lernmodell, um die Veränderung von Muskel- und Fettmasse über einen Zeitraum von drei Monaten vorherzusagen. Es basiert auf der mathematischen Gleichung einer wissenschaftlichen Studie und kombiniert deterministisch berechnete Daten mit zufällig generierten Werten, um ein robustes Trainingsdatenset zu erstellen.

---

## Projektstruktur
- **`data_generation.py`**: Generiert Trainingsdaten (deterministisch und zufällig) und speichert sie in CSV-Dateien.
- **`train.py`**: Trainiert ein Feedforward-Neural-Network und speichert das Modell sowie die Skalierer.
- **`test_and_visualize.py`**: Testet das Modell, berechnet Fehler (MSE, MAE), und visualisiert die Ergebnisse.
- **`streamlit_app.py`**: Interaktive Benutzeroberfläche zur Eingabe von Daten und Vorhersage der Muskel- und Fettmasse.

---

## Installation
1. **Python installieren**: Version 3.8 oder höher.
2. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt

## Ausführung

1. ### Daten generieren:

   python data_generation.py

2. ### Model trainieren:

   python train.py

3. ### Model testen:

   python test_and_visualize.py

4. ### Streamlit starten:

   python streamlit_app.py

---

## Eingaben und Ausgaben

### **Eingaben:**
- **Geschlecht**: Auswahl zwischen "male" und "female".
- **Alter**: Ganzzahliger Wert (18 bis 100 Jahre).
- **Gewicht (kg)**: Dezimalwert (30.0 bis 200.0).
- **Körperfettanteil (%)**: Ganzzahliger Wert (5 bis 50).
- **Trainingsintensität**: Ganzzahliger Wert (1 bis 10, wobei 1 niedrig und 10 hochintensiv ist).
- **Trainingsfrequenz**: Ganzzahliger Wert (1 bis 7 Trainingstage pro Woche).
- **Tägliche Kalorienaufnahme**: Ganzzahliger Wert (1000 bis 5000 kcal).

### **Ausgaben:**
- **Veränderung der Muskelmasse (kg)**: Vorhergesagte Zunahme oder Abnahme der Muskelmasse.
- **Veränderung der Fettmasse (kg)**: Vorhergesagte Zunahme oder Abnahme der Fettmasse.
- **Dynamisches Feedback**: Kontextbasiertes Feedback, das auf den Vorhersagen basiert.

---

## Ergebnisse

- **Korrelation**: Perfekte Korrelation (1.00) zwischen den tatsächlichen und den vorhergesagten Werten. Dies reflektiert die hohe Präzision des Modells innerhalb der Trainingsdatenstruktur.
- **Visualisierung**: Darstellung der wahren und vorhergesagten Werte in `test_and_visualize.py`, einschliesslich Scatterplots für Lean Mass und Fat Mass.

---

## Verbesserungspotential

- **Validierung mit echten Daten**: Das Modell wurde ausschliesslich auf synthetischen Daten trainiert. Echte Daten könnten die Vorhersagefähigkeit und Robustheit verbessern.
- **Realistischere Szenarien**: Erweiterung des Modells, um Szenarien ausserhalb der Studienannahmen abzudecken, wie etwa genetische Variationen oder adaptive Veränderungen.

---

---

## Kontakt

- **Name**: Armor Ajdini  
- **E-Mail**: armor.ajdini@students.fhnw.ch 

Bitte zögern Sie nicht, mich bei Fragen zu kontaktieren.

---
