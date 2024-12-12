# Handwritten Syllable Classification: A Neglected Area of Research

This repository contains the source code and dataset used in the **Handwritten Syllable Classification** project. The aim of this project is to address the challenges in handwritten syllable classification in Indian regional languages, specifically in **Abugida scripts**. The project implements **Transfer Learning** using well-known models like **Xception**, **InceptionV3**, and **EfficientNetV2S** to classify syllables.

## Table of Contents
1. [Introduction](#introduction)
2. [Motivation](#motivation)
3. [Objectives](#objectives)
4. [Methodology](#methodology)
5. [Models and Results](#models-and-results)
6. [Future Scope](#future-scope)

---

## Introduction
The objective of the project is to classify handwritten syllables, which have not been explored much compared to the extensive research done on handwritten character recognition in the **English** language. This project focuses on creating a dataset and implementing **Transfer Learning** for **Indian regional languages** using **Abugida scripts**.

---

## Motivation
With the increasing demand for digitizing regional languages for documents like **bank papers, certificates**, etc., there is a growing need for robust handwritten syllable classification systems. However, research and publicly available datasets in this area are lacking, creating a gap that this project aims to fill.

---

## Objectives
The primary objectives of this project are:
1. **Dataset Generation**: Creation of a dataset using an Android application with specific features for handwritten syllable generation.
2. **Data Augmentation and Preprocessing**: Employing augmentation techniques to create a robust dataset and preparing it for model training.
3. **Model Training**: Using transfer learning techniques to train models on the dataset.
4. **Evaluation**: Assessing the models' performance using metrics such as **Accuracy, Precision, Recall, and AUC**.

---

## Methodology

1. **Dataset Generation**:
   - Used an **Android app** for creating the handwritten syllable dataset.
   - Features include **random stroke width**, **save and clear** buttons for seamless data creation.
   
2. **Preprocessing**:
   - Applied **data augmentation** such as **rotation**, **shearing**, and **zooming** to increase variability.
   - Added **padding** and converted the images to **RGB** format.

3. **Models Used**:
   - **Xception**
   - **InceptionV3**
   - **EfficientNetV2S**

---

## Models and Results
### Evaluation Metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **AUC (Area Under the Curve)**

| Model             | Train Accuracy (%) | Test Accuracy (%) | Precision (%) | Recall (%) | AUC (%)  |
|-------------------|--------------------|-------------------|---------------|------------|----------|
| Xception          | 96.52              | 92.65             | 92.57         | 92.30      | 99.71    |
| InceptionV3       | 94.59              | 91.02             | 92.65         | 91.02      | 99.76    |
| EfficientNetV2S   | 90.29              | 85.47             | 88.72         | 87.47      | 99.30    |

### Visualizations:
- **t-SNE** and **UMAP** plots show that syllable classes are visually similar but less clustered compared to Mnist digits.

---

## Future Scope
- **Expand Dataset**: Gather more handwritten syllables from different individuals for more variability.
- **Synthetic Dataset**: Explore creating a synthetic dataset for further analysis.
- **Experimentation**: Train models from scratch and fine-tune hyperparameters for better results.

---
