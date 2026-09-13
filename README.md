# ❤️ Couple Love Prediction Model

A Machine Learning project that predicts a **Love Score** based on relationship-related factors such as communication, trust, understanding, time spent together, support, fights, gifts, and happiness.

## 🚀 Project Overview

The Couple Love Prediction Model uses **Linear Regression** to estimate a love score from different relationship attributes.

The project demonstrates the complete Machine Learning workflow:

* Data preprocessing
* Exploratory Data Analysis
* Feature selection
* Model training
* Model evaluation
* Model serialization using Joblib
* Interactive prediction using Streamlit

## 📊 Features Used

* Communication Score
* Trust Score
* Understanding Score
* Time Together (Hours)
* Support Score
* Fights Per Month
* Gifts Per Month
* Happy Together Score

### 🎯 Target

**Love Score**

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

* Test Size: 20%
* Random State: 42
* Evaluation Metrics: MSE and R² Score

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* GitHub

## 📁 Project Structure

```text
couple-love-model/
│
├── app.py
├── model.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Vanshrajpu/couple-love-model.git
```

### 2. Open the project folder

```bash
cd couple-love-model
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

## 🌐 Deployment

The application can be deployed using **GitHub + Streamlit Community Cloud**.

The trained model is stored in `model.pkl` and loaded into the Streamlit application using Joblib.

## 🎯 Project Objective

The objective of this project is to demonstrate how Machine Learning can analyze multiple relationship factors and generate a predicted love score through an interactive web application.

## 🔮 Future Improvements

* Compare multiple Machine Learning algorithms
* Improve prediction accuracy
* Add more relationship features
* Add interactive visualizations
* Improve UI/UX
* Deploy the application online

## 👨‍💻 Author

**Vansh Rajput**

GitHub: **Vanshrajpu**

Interested in **Data Analysis, Machine Learning, and AI**.

---

⭐ If you found this project useful, consider giving the repository a star!
