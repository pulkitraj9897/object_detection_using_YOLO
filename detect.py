from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

model = YOLO('yolov8n.pt')

image_path = ''
results = model.predict(image_path)

result = result2[0]

img_with_boxes = result.plot()

plt.figure(figsize=(12, 12))
plt.imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)) 
plt.title("YOLOv8 Detection Results")
plt.axis('off') 
plt.show()