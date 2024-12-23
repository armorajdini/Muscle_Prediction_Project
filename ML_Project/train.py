import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib

def train_model():
    # Daten laden
    data = pd.read_csv("combined_data.csv")
    X = data[["gender", "age", "lean_mass", "fat_mass", "intensity", "frequency", "calories"]]
    y = data[["delta_lean_mass", "delta_fat_mass"]]

    # Kategorische Variable umwandeln
    X["gender"] = X["gender"].apply(lambda x: 1 if x == "male" else 0)

    # Daten skalieren
    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)

    # Modell definieren
    model = Sequential([
        Dense(128, activation="relu", input_dim=X_scaled.shape[1]),
        Dense(64, activation="relu"),
        Dense(32, activation="relu"),
        Dense(2)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    # Modell trainieren
    model.fit(X_scaled, y_scaled, epochs=100, batch_size=32, validation_split=0.2)

    # Modell und Skalierer speichern
    model.save("saved_model.keras")
    joblib.dump(scaler_X, "scaler_X.pkl")
    joblib.dump(scaler_y, "scaler_y.pkl")

    print("Training abgeschlossen und Modell sowie Skalierer gespeichert.")

if __name__ == "__main__":
    train_model()