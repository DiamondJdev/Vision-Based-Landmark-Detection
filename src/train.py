from ultralytics import YOLO

model = YOLO("yolov8n-obb.yaml").load("yolov8n-obb.pt")

results = model.train(
    optimizer='SGD',  # Change optimizer
    name="exp1",
    project="runs/DOTAV1.5",
    data="DOTAv1.5.yaml",
    epochs=5,
    warmup_epochs=1,
    imgsz=640,
    batch=48,
    workers=4,
    val=True,
    cache=True,
    lr0=0.001,  # Adjust learning rate
    amp=True
)
print(results)
model.save("yolov8n-obb-trained.pt")