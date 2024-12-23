import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Laden des Modells und der Skalierer
model = load_model("saved_model.keras")
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")

# Titel und Layout
st.title("Muskel- und Fettmasse Vorhersage")
st.markdown("""
Dieses Tool berechnet die Veränderungen der Muskel- und Fettmasse über einen Zeitraum von 3 Monaten basierend auf Ihren Eingaben.
""")

# Layout: Zwei Spalten
left_col, right_col = st.columns(2)

with left_col:
    st.header("Eingabeparameter")

    # Benutzereingaben
    gender = st.selectbox("Geschlecht", options=["male", "female"])
    age = st.number_input("Alter", min_value=18, max_value=100, value=25, step=1)
    weight = st.number_input("Gewicht (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
    body_fat_percentage = st.slider("Körperfettanteil (%)", min_value=5, max_value=50, value=20)
    intensity = st.slider("Trainingsintensität (1-10)", min_value=1, max_value=10, value=5)
    frequency = st.slider("Trainingstage pro Woche", min_value=1, max_value=7, value=3)
    calories = st.number_input("Tägliche Kalorienaufnahme", min_value=1000, max_value=5000, value=2500)

    # Umrechnungen
    lean_mass = weight * (1 - body_fat_percentage / 100)
    fat_mass = weight * (body_fat_percentage / 100)

    # Eingabedaten formatieren
    user_input = pd.DataFrame({
        "gender": [1 if gender == "male" else 0],
        "age": [age],
        "lean_mass": [lean_mass],
        "fat_mass": [fat_mass],
        "intensity": [intensity],
        "frequency": [frequency],
        "calories": [calories]
    })

    st.write("Umgerechnete Werte:")
    st.write(f"Lean Mass (kg): {lean_mass:.2f}")
    st.write(f"Fat Mass (kg): {fat_mass:.2f}")

with right_col:
    st.header("Vorhersage")

    # Skalierung und Vorhersage
    user_input_scaled = scaler_X.transform(user_input)
    prediction_scaled = model.predict(user_input_scaled)
    prediction = scaler_y.inverse_transform(prediction_scaled)

    # Ergebnisse anzeigen
    st.subheader("Ergebnisse:")
    delta_lean_mass = prediction[0][0]
    delta_fat_mass = prediction[0][1]

    st.metric("Veränderung Lean Mass (kg)", f"{delta_lean_mass:.2f}")
    st.metric("Veränderung Fat Mass (kg)", f"{delta_fat_mass:.2f}")

    # Feedback
    st.markdown("---")
    if delta_lean_mass > 0 and delta_fat_mass <= 0:
        feedback = "Gute Arbeit! Ihr Training und Ernährungsplan unterstützt den Muskelaufbau und Fettabbau."
    elif delta_lean_mass > 0 and delta_fat_mass > 0:
        feedback = "Sie bauen Muskeln auf, achten Sie jedoch auf einen möglichen Fettzuwachs."
    elif delta_lean_mass <= 0 and delta_fat_mass <= 0:
        feedback = "Sie verlieren Gewicht. Stellen Sie sicher, dass Sie genug trainieren, um Muskeln zu erhalten."
    else:
        feedback = "Überprüfen Sie Ihren Ernährungs- und Trainingsplan, da Muskelabbau und Fettzunahme nicht ideal sind."

    st.write(feedback)