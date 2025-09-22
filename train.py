from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Train the model using your dataset
results = model.train(data='ppe_data.yaml', epochs=100, imgsz=640, batch=8)