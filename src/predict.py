from ultralytics import YOLO

model = YOLO("./runs/DOTAV1.5/exp1/weights/best.pt")
if input() == 'video':
    image_path = 'Yuneec Typhoon Q500 4K Drone Parking Lot Cruising.mp4'
else:
    image_path = "../images/Tenis.png"

results = model.predict(source=image_path, conf=0.005, show=True, save=True, save_txt=True)

# Display results in the terminal
for result in results:
    print(f"Image: {result.path}")
    if result.boxes is not None:  # Check if detections exist
        print(f"Detected objects: {len(result.boxes)}")
        for box in result.boxes:
            print(f" - Class: {box.cls}, Confidence: {box.conf:.2f}, Coordinates: {box.xyxy.numpy()}")
    else:
        print("No objects detected.")
# image_path = "C:/Users/diamo/PycharmProjects/Vision-Based-Landmark-Detection/images/lot_of_cars_angled.png"
# results = model.predict(source=image_path, conf=0.1, show=True, save=True, save_txt=True)
#
# # Display results in the terminal
# if results is None:
#     exit(1)
# for result in results:
#     print(f"Image: {result.path}")
#     print(f"Detected objects: {len(result.boxes)}")
#     for box in result.boxes:
#         print(f" - Class: {box.cls}, Confidence: {box.conf:.2f}, Coordinates: {box.xyxy.numpy()}")

# The predictions (annotated images) will be saved in a 'runs/predict' directory by default
