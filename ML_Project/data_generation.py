import numpy as np
import pandas as pd

# Funktion zur Berechnung von Muskel- und Fettveränderung basierend auf der Gleichung
def simulate_changes(gender, lean_mass, fat_mass, intensity, frequency, protein_effect, age, calories):
    if gender == "male":
        r, H1, H2 = 0.25, 66, 74
    else:
        r, H1, H2 = 0.21, 42, 28

    age_effect = max(0.9, 1 - (age - 30) * 0.01)
    delta_lean_mass = (
        r
        * (lean_mass / (lean_mass + H1))
        * (1 / (1 + lean_mass / H2))
        * intensity
        * frequency
        * protein_effect
        * age_effect
        + 0.01 * (calories - 2500)
    )

    delta_fat_mass = 0.02 * (calories - 2500) - 0.1 * delta_lean_mass
    return delta_lean_mass, delta_fat_mass

# Funktion zur Generierung deterministischer Daten
def generate_deterministic_data(n_samples=100000):
    data = []
    genders = ["male", "female"]
    ages = np.linspace(18, 65, 20)
    lean_masses = np.linspace(30, 100, 20)
    fat_masses = np.linspace(5, 50, 20)
    intensities = range(1, 6)
    frequencies = range(1, 6)
    calorie_levels = np.linspace(1500, 4000, 10)

    for gender in genders:
        for age in ages:
            for lean_mass in lean_masses:
                for fat_mass in fat_masses:
                    for intensity in intensities:
                        for frequency in frequencies:
                            for calories in calorie_levels:
                                protein_effect = 1.0
                                delta_lean_mass, delta_fat_mass = simulate_changes(
                                    gender, lean_mass, fat_mass, intensity, frequency, protein_effect, age, calories
                                )
                                data.append(
                                    [gender, age, lean_mass, fat_mass, intensity, frequency, calories, delta_lean_mass, delta_fat_mass]
                                )
                                if len(data) >= n_samples:
                                    break
                            if len(data) >= n_samples:
                                break
                        if len(data) >= n_samples:
                            break
                    if len(data) >= n_samples:
                        break
                if len(data) >= n_samples:
                    break
            if len(data) >= n_samples:
                break
    columns = [
        "gender", "age", "lean_mass", "fat_mass", "intensity", "frequency", "calories", "delta_lean_mass", "delta_fat_mass"
    ]
    return pd.DataFrame(data, columns=columns)

# Funktion zur Generierung zufälliger Daten
def generate_random_data(n_samples=100000):
    data = []
    for _ in range(n_samples):
        gender = np.random.choice(["male", "female"])
        age = np.random.randint(18, 66)
        lean_mass = np.random.uniform(30, 100)
        fat_mass = np.random.uniform(5, 50)
        intensity = np.random.randint(1, 11)
        frequency = np.random.randint(1, 6)
        calories = np.random.randint(1500, 4000)
        protein_effect = np.random.uniform(0.8, 1.2)

        delta_lean_mass, delta_fat_mass = simulate_changes(
            gender, lean_mass, fat_mass, intensity, frequency, protein_effect, age, calories
        )
        data.append(
            [gender, age, lean_mass, fat_mass, intensity, frequency, calories, delta_lean_mass, delta_fat_mass]
        )
    columns = [
        "gender", "age", "lean_mass", "fat_mass", "intensity", "frequency", "calories", "delta_lean_mass", "delta_fat_mass"
    ]
    return pd.DataFrame(data, columns=columns)

# Daten generieren und speichern
if __name__ == "__main__":
    df_deterministic = generate_deterministic_data(n_samples=100000)
    df_random = generate_random_data(n_samples=100000)
    combined_data = pd.concat([df_deterministic, df_random], ignore_index=True)
    df_deterministic.to_csv("deterministic_data.csv", index=False)
    df_random.to_csv("random_data.csv", index=False)
    combined_data.to_csv("combined_data.csv", index=False)
    print("Daten generiert und gespeichert!")