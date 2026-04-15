# Plant Disease Prediction using Deep Learning

## Project Overview

This project is a **Plant Disease Prediction System** built using Deep Learning. It takes an image of a plant leaf as input and predicts the disease affecting the plant. The goal is to help farmers and researchers identify plant diseases early and take appropriate action.

---

## Features

* Upload plant leaf images for prediction
* Deep learning model trained on plant disease dataset
* Accurate classification of multiple plant diseases
* Interactive web app using Streamlit
* Visualization of model performance (accuracy, loss, confusion matrix)

---

## Model Details

* Framework: TensorFlow / Keras
* Model Type: Convolutional Neural Network (CNN)
* Input: Leaf images
* Output: Predicted plant disease class

---

## Project Structure

```
plant_disease_detection/
│
├── train/                     # Training dataset
├── valid/                     # Validation dataset
├── test/                      # Testing dataset
├── Test_plant_disease.ipynb   # Model testing notebook
├── training_plant_disease_prediction.ipynb  # Training notebook
├── training_hist.json         # Training history
├── main.py                    # Streamlit web app
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## Dataset Information

This dataset is recreated using **offline augmentation** from the original dataset.

* Contains **~87,000 RGB images** of plant leaves
* Includes both **healthy and diseased leaves**
* Categorized into **38 different classes**

### Dataset Split

* **Training Set (80%)** → Used to train the model
* **Validation Set (20%)** → Used to evaluate performance during training
* **Test Set** → Contains **33 images** used for prediction/testing

### Source

* Kaggle Dataset: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset
* Based on the original PlantVillage dataset

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/plant-disease-prediction.git
cd plant-disease-prediction
```

### 2. Create environment (Anaconda recommended)

```bash
conda create -n tensorflow_env python=3.10
conda activate tensorflow_env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the Project

###  Run Jupyter Notebook

```bash
jupyter notebook
```

### Run Streamlit Web App

```bash
streamlit run main.py
```

---

## How to Use

1. Open the Streamlit app
2. Upload a plant leaf image
3. Click on Detect
4. View the predicted disease

---

## Model Evaluation

* Accuracy and Loss graphs
* Precision, Recall, F1 Score

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* OpenCV
* Streamlit

---

## Limitations

* Model accuracy depends on dataset quality
* May not generalize well to unseen plant species
* Requires good quality images for better prediction

---

## Future Improvements

* Add more plant species and diseases
* Improve model accuracy using advanced architectures
* Deploy the app online
* Add real-time camera prediction

---

## License

This project is for educational purposes.

---

## Acknowledgements

* Dataset providers
* Open-source libraries used in the project
