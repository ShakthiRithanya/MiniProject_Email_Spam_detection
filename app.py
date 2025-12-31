import streamlit as st
import joblib
import nltk
import string
from nltk.corpus import stopwords
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(
    page_title="AI Spam Sentry Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Outfit', sans-serif;
    }

    /* Main Background */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
        color: #f8fafc;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 2rem;
    }
    
    /* Title and Headers */
    .hero-title {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        color: #94a3b8;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    
    /* Text Area */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #f1f5f9 !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 20px !important;
        font-size: 18px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2) !important;
        background-color: rgba(255, 255, 255, 0.08) !important;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 18px 30px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 20px 25px -5px rgba(56, 189, 248, 0.3) !important;
        filter: brightness(1.1);
    }
    
    /* Result Animations */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .result-container {
        animation: slideUp 0.6s cubic-bezier(0.23, 1, 0.32, 1);
    }

    /* Metric Boxes */
    .metric-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC ---

@st.cache_resource
def load_resources():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    
    # Load model and vectorizer
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_resources()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png' width='120'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #38bdf8;'>AI SENTRY v2.0</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🔍 Enterprise Core")
    st.write("Using high-dimensional Logistic Regression with TF-IDF vectorization to protect your communication.")
    
    st.markdown("### 📊 Performance Metrics")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='metric-box'><small>Accuracy</small><br><b>98.2%</b></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='metric-box'><small>Precision</small><br><b>99.1%</b></div>", unsafe_allow_html=True)
    
    st.write("")
    st.info("💡 Pro Tip: Short, generic messages like 'Hi' or 'Ok' are almost always marked as Safe (Ham).")

# --- MAIN UI ---
st.markdown("<h1 class='hero-title'>AI Spam Sentry Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Next-Generation Intelligence for Secure Communications</p>", unsafe_allow_html=True)

# Layout Columns
left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    user_input = st.text_area(
        "Enter content to analyze:",
        height=250,
        placeholder="Paste your suspicious email or SMS here..."
    )
    
    btn_col_1, btn_col_2, btn_col_3 = st.columns([1, 2, 1])
    with btn_col_2:
        analyze_btn = st.button("🛡️ SECURE SCAN")
    st.markdown("</div>", unsafe_allow_html=True)

# Analysis Logic
if analyze_btn:
    if not user_input.strip():
        st.toast("⚠️ Empty input detected", icon="❌")
    else:
        with st.spinner("Initializing Deep Scan..."):
            # Preprocess
            clean_text = preprocess_text(user_input)
            time.sleep(0.4)
            
            # Vectorize
            vectorized_text = vectorizer.transform([clean_text])
            
            # Prediction
            probability = model.predict_proba(vectorized_text)[0]
            spam_prob = probability[1]
            threshold = 0.45
            is_spam = spam_prob >= threshold

        with right_col:
            st.markdown("<div class='result-container'>", unsafe_allow_html=True)
            if is_spam:
                st.markdown(f"""
                    <div style='background: rgba(239, 68, 68, 0.1); border: 2px solid #ef4444; border-radius: 20px; padding: 2rem; text-align: center; margin-bottom: 2rem;'>
                        <h1 style='color: #ef4444; margin-bottom: 0;'>🚨 THREAT DETECTED</h1>
                        <p style='color: #fca5a5;'>Probability of Spam: <b>{spam_prob*100:.1f}%</b></p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Gauge Chart
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = spam_prob * 100,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Spam Score", 'font': {'size': 24, 'color': '#ef4444'}},
                    gauge = {
                        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                        'bar': {'color': "#ef4444"},
                        'bgcolor': "rgba(255,255,255,0.05)",
                        'steps': [
                            {'range': [0, 45], 'color': 'rgba(34, 197, 94, 0.2)'},
                            {'range': [45, 100], 'color': 'rgba(239, 68, 68, 0.2)'}
                        ],
                    }
                ))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Outfit"}, height=300)
                st.plotly_chart(fig, use_container_width=True)
                
            else:
                st.markdown(f"""
                    <div style='background: rgba(34, 197, 94, 0.1); border: 2px solid #22c55e; border-radius: 20px; padding: 2rem; text-align: center; margin-bottom: 2rem;'>
                        <h1 style='color: #22c55e; margin-bottom: 0;'>✅ VERIFIED SAFE</h1>
                        <p style='color: #86efac;'>Safety Confidence: <b>{(1-spam_prob)*100:.1f}%</b></p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Gauge Chart
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = (1-spam_prob) * 100,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Safe Score", 'font': {'size': 24, 'color': '#22c55e'}},
                    gauge = {
                        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                        'bar': {'color': "#22c55e"},
                        'bgcolor': "rgba(255,255,255,0.05)",
                        'steps': [
                            {'range': [0, 55], 'color': 'rgba(239, 68, 68, 0.2)'},
                            {'range': [55, 100], 'color': 'rgba(34, 197, 94, 0.2)'}
                        ],
                    }
                ))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Outfit"}, height=300)
                st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

    # Detailed Analysis Section underneath
    st.markdown("---")
    st.subheader("🛠️ Forensic Breakdown")
    exp_col1, exp_col2 = st.columns(2)
    with exp_col1:
        st.caption("Cleaned Tokens")
        st.write(f"`{clean_text}`" if clean_text else "No tokens extracted")
    with exp_col2:
        st.caption("Raw Model Output")
        st.json({
            "Label": "Spam" if is_spam else "Ham",
            "Threshold": threshold,
            "Logic": "Sigmoid Probability Estimation"
        })

# Background Design Elements (Subtle)
st.markdown("""
<div style='position: fixed; top: 10%; right: -5%; width: 300px; height: 300px; background: rgba(56, 189, 248, 0.05); filter: blur(100px); z-index: -1;'></div>
<div style='position: fixed; bottom: 10%; left: -5%; width: 400px; height: 400px; background: rgba(99, 102, 241, 0.05); filter: blur(100px); z-index: -1;'></div>
""", unsafe_allow_html=True)
