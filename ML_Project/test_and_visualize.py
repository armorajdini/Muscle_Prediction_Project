import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib

# Modell und Skalierer laden
model = load_model("saved_model.keras")
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")

# Daten laden
data = pd.read_csv("combined_data.csv")

# Features und Ziele definieren
X = data[["gender", "age", "lean_mass", "fat_mass", "intensity", "frequency", "calories"]]
y_true = data[["delta_lean_mass", "delta_fat_mass"]]

# Kategorische Variable umwandeln
X = X.copy()  # Sicherstellen, dass keine unerwünschten Änderungen passieren
X["gender"] = X["gender"].apply(lambda x: 1 if x == "male" else 0)

# Daten skalieren
X_scaled = scaler_X.transform(X)
y_true_scaled = scaler_y.transform(y_true)

# Vorhersagen
y_pred_scaled = model.predict(X_scaled)
y_pred = scaler_y.inverse_transform(y_pred_scaled)

# Fehlerberechnung
mse = np.mean((y_true.values - y_pred) ** 2, axis=0)
mae = np.mean(np.abs(y_true.values - y_pred), axis=0)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")

# Visualisierung der Ergebnisse
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(y_true["delta_lean_mass"], y_pred[:, 0], alpha=0.6, label="Lean Mass")
plt.plot([y_true.values.min(), y_true.values.max()],
         [y_true.values.min(), y_true.values.max()], color="red", linestyle="--", label="Ideal")
plt.xlabel("True Lean Mass Change (kg)")
plt.ylabel("Predicted Lean Mass Change (kg)")
plt.title("Lean Mass: True vs Predicted")
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(y_true["delta_fat_mass"], y_pred[:, 1], alpha=0.6, label="Fat Mass")
plt.plot([y_true.values.min(), y_true.values.max()],
         [y_true.values.min(), y_true.values.max()], color="red", linestyle="--", label="Ideal")
plt.xlabel("True Fat Mass Change (kg)")
plt.ylabel("Predicted Fat Mass Change (kg)")
plt.title("Fat Mass: True vs Predicted")
plt.legend()

plt.tight_layout()
plt.show()

# Korrelation zwischen Vorhersagen und tatsächlichen Werten
lean_mass_corr = np.corrcoef(y_true["delta_lean_mass"], y_pred[:, 0])[0, 1]
fat_mass_corr = np.corrcoef(y_true["delta_fat_mass"], y_pred[:, 1])[0, 1]

print(f"Korrelation zwischen tatsächlicher und vorhergesagter Lean Mass Änderung: {lean_mass_corr:.2f}")
print(f"Korrelation zwischen tatsächlicher und vorhergesagter Fat Mass Änderung: {fat_mass_corr:.2f}")