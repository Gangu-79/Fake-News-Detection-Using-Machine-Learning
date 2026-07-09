# 📰 Fake News Detection Using Machine Learning

> A Machine Learning project developed using **IBM watsonx.ai Studio** to classify news articles as **Fake** or **Real** using Natural Language Processing (NLP) and Logistic Regression.

---

## 📖 Project Overview

The rapid spread of misinformation on social media and online platforms has become a major concern worldwide. This project uses **Machine Learning** and **Natural Language Processing (NLP)** to automatically classify news articles as **Fake** or **Real**.

The model was developed entirely in **IBM watsonx.ai Studio** and trained using the **Fake News Dataset** with Logistic Regression and TF-IDF Vectorization.

---

## 🎯 Objectives

- Detect fake news automatically.
- Reduce misinformation.
- Learn NLP techniques.
- Build a Machine Learning classification model.
- Deploy and develop the project using IBM watsonx.ai Studio.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| IBM watsonx.ai Studio | Development Environment |
| Pandas | Data Analysis |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | Feature Extraction |
| Logistic Regression | Classification |

---

# 📂 Dataset

The dataset consists of two files:

- Fake.csv
- True.csv

Each news article contains:

- Title
- News Content
- Subject
- Date

Labels:

- **0 → Fake News**
- **1 → Real News**

---

# 🔄 Project Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Train-Test Split
   │
   ▼
Logistic Regression
   │
   ▼
Prediction
   │
   ▼
Performance Evaluation
```

---

# 📊 Data Visualization

## 1️⃣ Number of Fake and Real News Articles

![Bar Chart](images/bar_chart.png)

This chart shows the total number of Fake and Real news articles available in the dataset.

---

## 2️⃣ Distribution of Fake and Real News

![Pie Chart](images/pie_chart.png)

The pie chart illustrates the percentage distribution of Fake and Real news articles in the dataset.

---

# 🤖 Machine Learning Model

Algorithm Used:

- Logistic Regression

Feature Extraction:

- TF-IDF Vectorizer

---

# 📈 Model Evaluation

The following evaluation metrics were used:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix

---

# 📁 Project Structure

```
Fake-News-Detection-Using-Machine-Learning/
│
├── FakeNewsDetection.ipynb
├── README.md
├── requirements.txt
├── images/
│   ├── bar_chart.png
│   └── pie_chart.png
└── Dataset Link
```

---

# 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Fake-News-Detection-Using-Machine-Learning.git
cd Fake-News-Detection-Using-Machine-Learning
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Notebook

Open

```
FakeNewsDetection.ipynb
```

and execute all cells.

---

## 🏗️ Django Web Application

This repository also includes a Django web app for fake news detection.

### Run the Django App

```bash
cd fakenews
python -m venv venv
.\venv\Scripts\activate
pip install -r ..\requirements.txt
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000/
```

### Web App Features

- Text input area for article or headline analysis
- Fake/Real prediction output
- Confidence score
- Responsive styled frontend with Django templates

---

# 📌 Applications

- Fake News Detection
- Social Media Monitoring
- News Verification
- Journalism
- Educational Research
- AI-based Fact Checking

---

# 🔮 Future Scope

- Deep Learning (LSTM)
- BERT Model
- Flask/Django Web App
- Real-Time News Prediction
- REST API
- Streamlit Dashboard

---

# 📚 Skills Demonstrated

- Machine Learning
- Natural Language Processing
- Data Visualization
- Logistic Regression
- Feature Engineering
- IBM watsonx.ai Studio
- IBM Cloud

---

# 🙏 Acknowledgements

- IBM watsonx.ai Studio
- IBM Cloud
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Kaggle Dataset

---

⭐ If you like this project, don't forget to Star the repository!
