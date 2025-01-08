import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import joblib  # For saving the trained model

# Dataset path
dataset_path = "C:/Users/girij/Distributed systems/Dataset/ai4agriculture_2020"

# Load images
data = []
labels = []
image_paths = []
for file_name in os.listdir(dataset_path):
    file_path = os.path.join(dataset_path, file_name)
    image = cv2.imread(file_path)
    if image is not None:
        image = cv2.resize(image, (224, 224))
        data.append(image)
        image_paths.append(file_path)

data = np.array(data)

# Extract features using MobileNetV2
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg", input_shape=(224, 224, 3))
features = model.predict(preprocess_input(data))

# Apply K-Means clustering
n_clusters = 3  # Healthy, Dry, Ripe
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(features)

# Save clustered images for manual inspection
for i, label in enumerate(cluster_labels):
    cluster_dir = os.path.join(dataset_path, f"cluster_{label}")
    os.makedirs(cluster_dir, exist_ok=True)
    file_name = os.path.basename(image_paths[i])
    cv2.imwrite(os.path.join(cluster_dir, file_name), data[i])

print("Clustering complete! Images saved into cluster directories.")

# Create labels for supervised training (optional)
for i, label in enumerate(cluster_labels):
    labels.append(label)  # Assign cluster labels as training labels

# Train a Random Forest Classifier
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Evaluate the classifier
accuracy = classifier.score(X_test, y_test)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(classifier, "trained_plant_model.pkl")
print("Model saved as trained_plant_model.pkl")
