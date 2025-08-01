# **Real-Time Object Detection with YOLOv8**

This project demonstrates a high-performance object detection system using **YOLOv8**, a state-of-the-art, real-time AI model. The system can identify and locate 80 different classes of common objects (e.g., people, cars, traffic lights, dogs) in images and video streams.

This implementation leverages a pre-trained model from ultralytics, showcasing the ability to rapidly prototype and deploy advanced computer vision solutions.

*(Replace the image URL above with a screenshot of your own results after you upload it to GitHub\!)*

## **Features**

* **State-of-the-Art Model:** Utilizes the YOLOv8n ('nano') model, known for its excellent balance of speed and accuracy.  
* **80 Object Classes:** Pre-trained on the comprehensive COCO dataset, enabling detection of a wide variety of objects.  
* **High Performance:** Processes images efficiently, making it suitable for real-time applications.  
* **Simple & Clean Code:** Demonstrates how to use a powerful AI model with a simple and accessible Python script.

## **Technology Stack**

* **Language:** Python 3.9+  
* **Core Libraries:**  
  * ultralytics: For the YOLOv8 model implementation.  
  * OpenCV-Python: For image handling.  
  * Matplotlib: For displaying results.  
* **Environment:** Anaconda / venv

## **Setup and Installation**

Follow these steps to set up the project environment and run the detection script.

**1\. Clone the repository:**

git clone https://github.com/pulkitraj9897/object\_detection\_using\_YOLO.git  
object\_detection\_using\_YOLO

2\. Create a Python Environment:  
It is highly recommended to use a virtual environment.  
*Using Anaconda:*

conda create \--name yolo\_env python=3.9  
conda activate yolo\_env

**3\. Install Dependencies:**

pip install \-r requirements.txt

## **Usage**

1. Place any image you want to test in the root directory of the project.  
2. Update the image\_path variable in the detect.py script to your image's filename.  
3. Run the script:  
   python detect.py  
4. The script will display the image with bounding boxes drawn around the detected objects.

## **Future Work**

* **Custom Model Training:** Fine-tune the YOLOv8 model on a custom dataset to detect specialized objects.  
* **Real-Time Webcam Feed:** Adapt the script to process a live video stream from a webcam.  
* **API Deployment:** Wrap the model in a Flask or FastAPI service to create a web-based API for object detection.