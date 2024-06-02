# Binary image classification for cancer detection

This repository contains an end-to-end pipeline for binary classification of images using transfer learning with the VGG16 model from Keras. The project is designed to cover the complete machine learning workflow, from data ingestion to model deployment.

## Features

- **Transfer Learning with VGG16**
  - Leverage the pre-trained VGG16 model to enhance classification accuracy and reduce training time.

- **End-to-End Pipeline**
  - **Data Ingestion**: Efficiently gather and manage the dataset.
  - **Data Transformation**: Preprocess and augment data to improve model performance.
  - **Model Training**: Train the VGG16 model on the prepared dataset.
  - **Model Deployment**: Deploy the trained model for real-world application.

- **Data Tracking with DVC**
  - Utilize Data Version Control (DVC) to track dataset changes and ensure reproducibility.

- **Experiment Tracking with MLflow**
  - Monitor and log experiments, model parameters, and results for comprehensive tracking and comparison.

- **Deployment with Jenkins**
  - Automate the deployment pipeline using Jenkins for continuous integration and delivery.

- **Flask App Hosted on AWS**
  - Serve the trained model via a Flask application hosted on AWS, enabling easy access and scalability.
