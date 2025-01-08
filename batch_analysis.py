import os
import cv2
import joblib
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Define the same classes as in the training script
classes = ["healthy", "dry", "ripe"]

# Load the trained model
model = joblib.load("C:/Users/girij/Distributed systems/trained_plant_model.pkl")

# Load the MobileNetV2 feature extractor
feature_extractor = MobileNetV2(weights="imagenet", include_top=False, pooling="avg", input_shape=(224, 224, 3))

# Directory containing images
image_dir = r"C:\Users\girij\Distributed systems\Dataset\ai4agriculture_2020"

# Predict on all images in the directory
def predict_grape_condition(image_path):
    """
    Predict the condition of a grape based on an input image.
    :param image_path: Path to the grape image.
    :return: Predicted condition.
    """
    # Load and preprocess the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot load image at path: {image_path}")
    image = cv2.resize(image, (224, 224))  # Resize image to match MobileNetV2 input size
    image = preprocess_input(np.expand_dims(image, axis=0))  # Preprocess for MobileNetV2

    # Extract features using MobileNetV2
    features = feature_extractor.predict(image)

    # Make prediction
    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])  # Get confidence score
    return {"status": classes[prediction], "confidence": confidence}

# Iterate through the directory and process each image
for file_name in os.listdir(image_dir):
    if file_name.endswith(".jpg"):  # Process only .jpg files
        image_path = os.path.join(image_dir, file_name)
        try:
            result = predict_grape_condition(image_path)
            print(f"Image: {file_name}, Predicted condition: {result['status']}, Confidence: {result['confidence']:.2f}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
