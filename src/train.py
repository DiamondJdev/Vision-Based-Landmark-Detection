import os.path

import torch
from ultralytics import YOLO
import wandb

wandb.init(project="yolo-drone-object-detection", name="YOLOv8_DOTAv1.5")

if os.path.exists("yolov8n-obb.pt"):
    model = YOLO("yolov8n-obb.yaml").load("yolov8n-obb.pt")
else:
    model = YOLO("yolov8n-obb.yaml")

results = model.train(
    optimizer='AdamW',  # Change optimizer
    name="exp1",
    project="runs/DOTAV1.5",
    data="DOTAv1.5.yaml",
    epochs=1,
    warmup_epochs=0,
    imgsz=640,
    batch=48,
    # workers=4,
    val=True,
    cache=True,
    lr0=0.001,  # Adjust learning rate
    lrf=0.1,
    # scheduler='cosine',
    # amp=True
)

model.save("yolov8n-obb.pt")
wandb.finish()