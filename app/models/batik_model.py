import pandas as pd
from tensorflow.keras.models import load_model

# Define paths for model and class names
# MODEL_PATH = "resnet152.h5"

# kalau menggunakan model resnet dengan augmentasi rotasi dan zoom
MODEL_PATH = "[withAugmentasiZoom_rotasi45_135]Resnet152.h5"

CLASS_NAMES_PATH = "app/data/class_names.csv"
CLASS_DESCRIPTIONS_PATH = "app/data/class_deskripsi.csv"

# Load the model
model = load_model(MODEL_PATH)

# Load class names
class_names = pd.read_csv(CLASS_NAMES_PATH)["Class Names"].values

# Load class descriptions
class_descriptions = pd.read_csv(CLASS_DESCRIPTIONS_PATH)


def get_model():
    """Return the loaded model."""
    return model


def get_class_names():
    """Return the array of class names."""
    return class_names


def get_class_description(index):
    """
    Mengembalikan baris lengkap untuk indeks kelas tertentu.

    Parameters:
    index (int): Indeks dari kelas.

    Returns:
    pandas.Series or None: Baris lengkap dari DataFrame yang sesuai dengan indeks kelas,
                           atau None jika tidak ada data yang cocok.
    """
    result = class_descriptions[class_descriptions["kode_batik"] == index]
    return result.iloc[0] if not result.empty else None
