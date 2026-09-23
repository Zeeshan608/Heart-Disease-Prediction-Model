# ❤️ Heart Disease Prediction Model

A machine learning web app that predicts the likelihood of heart disease from a patient's clinical data — built with **scikit-learn** and served through an interactive **Streamlit** dashboard.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/scikit--learn-ML%20Model-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

---

## 📋 Overview

Cardiovascular disease is one of the leading causes of death worldwide, and early risk detection can make a real difference. This project trains and compares several classification models on the **UCI Heart Disease dataset**, tunes the best-performing one, and wraps it in a clean, user-friendly web interface so anyone can get an instant risk estimate from basic clinical inputs.

> ⚠️ **Disclaimer:** This tool is built for educational and demonstration purposes only. It is **not** a medical diagnostic device and should never replace professional medical advice.

---

## ✨ Features

- 🧠 **Multiple models compared** — Logistic Regression, K-Nearest Neighbors, Decision Tree, Random Forest, and SVC
- 🎯 **Hyperparameter tuning** with `GridSearchCV` to squeeze out the best accuracy
- 📊 **~87% test accuracy** with the tuned Logistic Regression model
- 🖥️ **Interactive Streamlit UI** with a styled, three-column patient input form
- ⚡ **Instant predictions** with confidence scores
- 🎨 Clean, custom-styled interface with clear "High Risk" / "Low Risk" result cards

---

## 🗂️ Project Structure

```
Heart-Disease-Prediction-Model/
├── Heart_Disease_Prediction_Model.ipynb   # Data exploration, model training & evaluation
├── app.py                                 # Streamlit web application
├── heart_disease_data.csv                 # Dataset (UCI Heart Disease dataset)
├── heart_disease_model.pkl                # Trained & tuned model (saved with joblib)
├── requirements.txt                       # Python dependencies
└── README.md
```

---

## 🧬 Dataset

The model is trained on the well-known **UCI Heart Disease dataset**, using 13 clinical features:

| Feature | Description |
|---|---|
| `age` | Age in years |
| `sex` | Sex (1 = male, 0 = female) |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels colored by fluoroscopy |
| `thal` | Thalassemia |

**Target:** `1` = presence of heart disease, `0` = absence of heart disease

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/Zeeshan608/Heart-Disease-Prediction-Model.git
cd Heart-Disease-Prediction-Model
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501` 🎉

---

## 🧪 Model Training

The full training pipeline is documented in [`Heart_Disease_Prediction_Model.ipynb`](Heart_Disease_Prediction_Model.ipynb) and includes:

1. **Data loading & preprocessing** — cleaning, splitting into train/test sets
2. **Baseline comparison** across five classifiers
3. **Hyperparameter tuning** of the top model using `GridSearchCV`
4. **Evaluation** on a held-out test set
5. **Export** of the final model with `joblib`

| Model | Test Accuracy |
|---|---|
| **Logistic Regression (tuned)** | **~87%** |
| Random Forest | ~84% |
| Decision Tree | ~82% |
| SVC | ~70% |
| K-Nearest Neighbors | ~69% |

---

## 🖼️ How It Works

1. Enter the patient's clinical details in the sidebar form (age, blood pressure, cholesterol, etc.)
2. Click **🔍 Predict**
3. Instantly view a **High Risk** or **Low Risk** result, along with the model's confidence score

---

## 🛠️ Tech Stack

- **Python** — core language
- **scikit-learn** — model training & evaluation
- **pandas / NumPy** — data handling
- **Streamlit** — web app framework
- **joblib** — model serialization

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/Zeeshan608/Heart-Disease-Prediction-Model/issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — feel free to use it for learning and experimentation.

---

## 👤 Author

**Zeeshan Ahmad Akhtar**
GitHub: [@Zeeshan608](https://github.com/Zeeshan608)

---

<p align="center">Made with ❤️ and a bit of Machine Learning</p>
