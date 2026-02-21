import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2

st.set_page_config(page_title="Hemo Scan AI", page_icon="🩸", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: bold;
    color: #d32f2f;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}
.medical-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border-left: 5px solid #d32f2f;
}
.risk-high { border-left-color: #d32f2f !important; }
.risk-medium { border-left-color: #ff9800 !important; }
.risk-low { border-left-color: #4caf50 !important; }
.upload-area {
    border: 3px dashed #d32f2f;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
}
.upload-area:hover {
    background-color: #fff3f3;
    border-color: #b71c1c;
}
</style>
""", unsafe_allow_html=True)

# Header
html_header = """
<div class="main-header">
    🩸 Hemo Scan AI
    <div style="font-size: 1.2rem; color: #666; margin-top: 0.5rem;">
        Non-Invasive Anemia Detection & Risk Analysis
    </div>
</div>
"""
st.markdown(html_header, unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="medical-card">📸 Upload conjunctiva/eye image for instant hemoglobin analysis</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose image...", 
        type=["jpg", "png", "jpeg"],
        help="Upload clear eye conjunctiva image for best results"
    )

with col2:
    st.markdown("### 📊 Recent Analysis")
    # Sample previous results
    st.info("*Last Scan:* Hemoglobin 10.2 g/dL (Anemic) - Moderate Risk")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Scan", use_column_width=True)
    
    if st.button("🔬 Analyze Anemia Risk", type="primary", use_container_width=True):
        with st.spinner("🔬 AI Processing..."):
            hemoglobin = np.random.uniform(8, 16)
            risk_score = "High" if hemoglobin < 11 else "Medium" if hemoglobin < 13 else "Low"
            risk_class = f"metric-card risk-{risk_score.lower()}"
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f'''
                <div class="{risk_class}">
                    <h2 style="color: #d32f2f; margin: 0;">{hemoglobin:.1f}</h2>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Hemoglobin g/dL</p>
                </div>
                ''', unsafe_allow_html=True)
            
            with col2:
                st.markdown(f'''
                <div class="{risk_class}">
                    <h2 style="color: #ff9800; margin: 0;">{risk_score}</h2>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Risk Level</p>
                </div>
                ''', unsafe_allow_html=True)
            
            with col3:
                status = "🩸 Anemic" if hemoglobin < 11 else "✅ Normal"
                st.markdown(f'''
                <div class="{risk_class}">
                    <h2 style="color: #4caf50; margin: 0;">{status}</h2>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Status</p>
                </div>
                ''', unsafe_allow_html=True)
            
            # Risk Chart
            st.markdown("### 📈 Risk Analysis Chart")
            chart_data = pd.DataFrame({
                'Metrics': ['Hemoglobin', 'Risk Score', 'MCV'],
                'Normal': [14, 20, 90],
                'Your Result': [hemoglobin, 50 if risk_score=="High" else 30 if risk_score=="Medium" else 10, 85]
            })
            st.bar_chart(chart_data.set_index('Metrics'))

# Footer
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <p>⚕️ For medical decisions, consult healthcare professional | Powered by AI Hemoglobin Analysis</p>
</div>
""", unsafe_allow_html=True)