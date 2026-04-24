# 🎬 Movie Review Sentiment Classification

## 📖 Project Description
This project builds a **sentiment analysis model** to classify movie reviews as **positive** or **negative** using Natural Language Processing (NLP).

The pipeline follows a simple workflow:
- Text preprocessing
- Feature extraction using TF-IDF
- Classification using Logistic Regression

---

## ⚙️ Methodology

### 🔹 1. Text Preprocessing
The raw text data is cleaned using NLP techniques:
- Convert text to lowercase
- Remove punctuation and special characters
- Tokenize text into words
- Remove stopwords
- Apply stemming/lemmatization (optional)

---

### 🔹 2. Feature Extraction (TF-IDF)
Text data is transformed into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**:
- Captures importance of words
- Reduces impact of common words
- Creates a sparse feature matrix

---

### 🔹 3. Model Training (Logistic Regression)
A **Logistic Regression** model is used for classification:
- Suitable for binary classification
- Efficient and fast
- Works well with text data

---

### 🔹 4. Model Evaluation
The Model got
- Accuracy of 88%
- Precision of 88%

---
## 🚀 Model Deployment
The model is deployed and accessible here:  
👉 https://movie-review-analysis-stk5.onrender.com/

## 🛠️ Tech Stack
- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK / spaCy

---

## 📂 Project Structure
```
movie-review-classification/
│── notebooks/           # Jupyter notebooks
│── src/                 # Source code
│── model/               # Saved model
│── README.md
```

---

## 📊 Results
The model performs well in classifying movie reviews, demonstrating that TF-IDF combined with Logistic Regression is an effective baseline for sentiment analysis.

---

## 🚀 Future Improvements
- Try models like Naive Bayes, SVM
- Use n-grams for better context
- Apply deep learning (LSTM, BERT)
- Deploy using Streamlit or Flask

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests.

---

## ⭐ Support
If you found this project useful, give it a star!