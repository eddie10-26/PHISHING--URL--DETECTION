import streamlit as st
import joblib
from src.feature_extraction import extract_features

# Page Configuration
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)

# Load Trained Model
@st.cache_resource
def load_model():
    return joblib.load('phishing_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error("Model file not found! Please run train.py first.")

# Title & Description
st.title("🛡️ Phishing URL Detection System")
st.markdown("Enter a website URL below to analyze if it is **Legitimate** or a **Phishing Threat**.")

# Input Field
url_input = st.text_input("🌐 Website URL:", placeholder="https://example.com")

if st.button("🔍 Analyze URL", type="primary"):
    if url_input.strip() == "":
        st.warning("Please enter a valid URL.")
    else:
        # Extract features
        features = extract_features(url_input)
        
        # Prediction
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        
        confidence = probabilities[prediction] * 100
        
        st.markdown("---")
        st.subheader("📊 Analysis Results")
        
        if prediction == 1:
            st.error(f"🚨 **PHISHING DETECTED!** (Confidence: {confidence:.1f}%)")
            st.warning("⚠️ High Risk! This link exhibits suspicious characteristics commonly used in phishing attacks.")
        else:
            st.success(f"✅ **SAFE / LEGITIMATE URL** (Confidence: {confidence:.1f}%)")
            st.info("🔒 Low Risk! The URL structure matches standard legitimate web addresses.")
            
        # Feature Breakdown Expansion
        st.markdown("---")
        with st.expander("🔬 View Extracted Security Features"):
            feature_names = [
                "URL Length", "Has @ Symbol", "Has IP Address", "Subdomain Count",
                "Path Depth", "Has Suspicious Keywords", "Is HTTPS",
                "Has Hyphen in Domain", "Has Shortening Service", "Domain Length"
            ]
            
            for name, val in zip(feature_names, features):
                st.write(f"- **{name}:** `{val}`")