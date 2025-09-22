from ultralytics import YOLO
import os

# --- IMPORTANT ---
# You may need to update 'train' to your latest training folder (e.g., 'train2', 'train3').
# Look inside your 'runs/detect/' folder to find the correct one.
model_path = os.path.join('runs', 'detect', 'train4', 'weights', 'best.pt')

# Load your custom-trained model
model = YOLO(model_path)

# Specify the path to an image you want to test
source_image = os.path.join('archive', 'source_files', 'source_files', 'JapanPPE.mp4')

# Run inference on the source image
# The results with bounding boxes will be saved automatically
results = model.predict(source=source_image, save=True)

print(f"Prediction complete! Check the latest folder in 'runs/detect/' for your output image.")