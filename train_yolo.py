from ultralytics import YOLO

# 1. Load the YOLO model
model = YOLO("yolov8n.pt")  

# 2. Train the model
model.train(
    data="data.yaml",       # Path to your data.yaml file (define train/val paths and classes)
    epochs=50,              # Number of epochs to train
    batch=16,               # Batch size
    imgsz=640,              # Image size (resolution)
    project="yolo_train",   # Output folder for training results
    name="yolo_v11_train",  # Name of the training run
    pretrained=True         # Use pretrained weights as the starting point
)

# 3. Evaluate the model (optional)
metrics = model.val()
print("Validation Metrics:", metrics)

# 4. Export the model (for deployment)
model.export(format="onnx")  # Export trained model to ONNX format (or other formats like 'torchscript', 'engine')
