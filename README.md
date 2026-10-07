# 🛡️ Phishing URL Detection System using Machine Learning

A robust, machine learning-driven web application designed to identify malicious and phishing URLs in real-time. Built using Python, Scikit-Learn, and Streamlit, this system extracts structural features from web links to classify them accurately.

---

## 📌 Project Overview
Phishing attacks are one of the most common vectors for cyber threats. This project leverages supervised machine learning to distinguish between legitimate and phishing URLs by analyzing lexical and technical patterns without relying on slow external API lookups.

* **Dataset Size:** 50,000 balanced URL samples (Kaggle dataset)
* **Model Used:** Random Forest Classifier
* **Performance:** **78.08%** Precision & Accuracy
* **UI Framework:** Interactive Streamlit Dashboard

---

## ⚙️ Key Features & Feature Engineering
The detection pipeline extracts **10 key structural features** from any input URL:
1. `url_length` – Total length of the URL.
2. `hostname_length` – Length of the domain name.
3. `count_dots` – Frequency of `.` in the URL.
4. `count_hyphens` – Frequency of `-` in the domain or path.
5. `count_at` – Presence of `@` symbol (often used in obfuscation).
6. `count_question_mark` – Frequency of query parameters.
7. `count_percent` – Encoded characters presence.
8. `has_ip` – Detects raw IP addresses used instead of domain names.
9. `is_https` – Checks if HTTPS protocol is enforced.
10. `count_digits` – Numerical character density.

---

## 📁 Project Structure
```text
PHISHING DETECTION/
├── .gitignore
├── app.py                      # Streamlit interactive UI dashboard
├── phishing_model.pkl          # Trained Random Forest model binary
├── requirements.txt            # Python environment dependencies
└── src/
    ├── feature_extraction.py   # URL feature engineering pipeline
    └── train.py                # Model training & evaluation script