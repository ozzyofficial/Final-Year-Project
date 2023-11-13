# README for Face Mask Detection System

## Introduction
This repository contains the implementation of a face mask detection system using the MobileNetV2 machine learning model. The system was developed in response to the COVID-19 pandemic to enforce the use of face masks in public places.

## Analysis of Existing System
In the early stages of the COVID-19 lockdown, face mask compliance was monitored physically, leading to potential human errors. Attempts were made to automate this process using AI, but existing solutions faced accuracy and deployment challenges.

## Proposed System
The proposed system employs the MobileNetV2 model, chosen for its accuracy and computational efficiency. Developed through Python and various libraries, the system undergoes data collection, pre-processing, training, testing, and evaluation phases.

## Benefits of the Proposed System
1. **Cost-Effective Development and Deployment:** Reduces costs during development and deployment.
2. **High Accuracy:** Achieves satisfactory levels of accuracy.
3. **Cross-Platform Deployment:** Can be deployed on various platforms, including Google mobile platforms.
4. **Reduced Human Error:** Minimizes the level of human error.
5. **Fast and Memory-Efficient:** Faster than previous systems and allows for memory-efficient inference.

## Model Development
### Data Collection
The dataset, obtained from Kaggle, comprises images of people with and without face masks.

### Data Pre-processing
Utilizing the Keras library, the images are converted into arrays, and one-hot encoding is applied to labels. Data is preprocessed for training and testing.

### Model Training
The MobileNetV2 model is trained using TensorFlow, Keras, sklearn, imutils, and numpy. The model undergoes data augmentation to enhance training.

### Model Testing
The trained model is tested on video frames using a webcam. Face detections are made, and predictions are displayed with bounding boxes.

### Model Evaluation
The model's accuracy and performance are evaluated using Sci-kit Learn and matplotlib to generate scores and visualizations.

## System Implementation and Results
### Installation Requirements
#### Hardware Requirements
- Laptop or desktop computer (64-bit)
- Webcam
- RAM: 8 GB minimum
- Processor: Intel Core i5, 2.4 GHz minimum

#### Software Requirements
- Operating System: Windows 10 or higher
- Python
- IDE: PyCharm, Jupyter notebook, etc.

### Model Development
The MobileNetV2 model was developed through stages, including data collection, pre-processing, training, evaluation, and testing. The README provides detailed steps and figures for each stage.

Feel free to explore the code and adapt it to your needs. For issues or improvements, please open an [issue](https://github.com/ozzyofficial/Final-Year-Project/issues) or submit a [pull request](https://github.com/ozzyofficial/Final-Year-Project/pulls).
