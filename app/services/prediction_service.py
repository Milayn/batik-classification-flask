import numpy as np
import tensorflow as tf
from app.models.batik_model import get_model, get_class_names

# Load the model
model = get_model()
class_names = get_class_names()


def load_and_preprocess_image(image_path, target_size=(512, 512)):
    """Load and preprocess image for prediction."""
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet.preprocess_input(img_array)
    return img_array


def predict_batik(image_path):
    """Predict the class of the image and display the top 5 predictions."""
    img_array = load_and_preprocess_image(image_path)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions, axis=1)[0]]

    return predicted_class
