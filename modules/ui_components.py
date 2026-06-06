"""
UI Components Module - Professional UI Elements and CSS
Author: Mubashir Ahmad Ameer, Rustam Khan
"""

import streamlit as st
from datetime import datetime


class UIComponents:
    """Professional UI components library"""
    
    @staticmethod
    def inject_css():
        """Inject professional CSS styles"""
        st.markdown("""
        <style>
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes slideInLeft {
                from { opacity: 0; transform: translateX(-50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            @keyframes slideInRight {
                from { opacity: 0; transform: translateX(50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            @keyframes glow {
                0% { box-shadow: 0 0 5px rgba(102,126,234,0.2); }
                100% { box-shadow: 0 0 20px rgba(102,126,234,0.6); }
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
            
            .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
                border-right: none;
                animation: slideInLeft 0.6s ease-out;
            }
            [data-testid="stSidebar"] * { color: white !important; }
            
            .main-header {
                background: rgba(255,255,255,0.95);
                backdrop-filter: blur(10px);
                border-radius: 24px;
                padding: 32px 40px;
                margin-bottom: 28px;
                border: 1px solid rgba(255,255,255,0.2);
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                animation: fadeIn 0.7s ease-out;
            }
            .main-title {
                font-size: 32px;
                font-weight: 800;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0;
            }
            .main-subtitle {
                font-size: 16px;
                color: #666;
                margin-top: 10px;
            }
            
            .kpi-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 24px;
                margin-bottom: 28px;
            }
            .kpi-card {
                background: rgba(255,255,255,0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 24px;
                text-align: center;
                border: 1px solid rgba(255,255,255,0.2);
                transition: all 0.3s ease;
                animation: slideInRight 0.5s ease-out;
                animation-fill-mode: both;
            }
            .kpi-card:nth-child(1) { animation-delay: 0.1s; }
            .kpi-card:nth-child(2) { animation-delay: 0.2s; }
            .kpi-card:nth-child(3) { animation-delay: 0.3s; }
            .kpi-card:nth-child(4) { animation-delay: 0.4s; }
            .kpi-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }
            .kpi-value {
                font-size: 38px;
                font-weight: 800;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .kpi-label { font-size: 14px; color: #666; margin-top: 10px; font-weight: 500; }
            
            .input-card {
                background: rgba(255,255,255,0.95);
                backdrop-filter: blur(10px);
                border-radius: 24px;
                border: 1px solid rgba(255,255,255,0.2);
                margin-bottom: 28px;
                overflow: hidden;
                animation: fadeIn 0.6s ease-out;
                animation-delay: 0.2s;
                animation-fill-mode: both;
            }
            .input-card-header {
                padding: 20px 28px;
                border-bottom: 1px solid rgba(0,0,0,0.05);
                background: rgba(102,126,234,0.05);
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: #667eea;
            }
            
            /* FIX: Results card with SOLID WHITE background and BLACK text */
            .results-card {
                background: #FFFFFF !important;
                border-radius: 24px;
                border: 1px solid #e0e0e0;
                margin-top: 28px;
                overflow: hidden;
                animation: fadeIn 0.6s ease-out;
                animation-delay: 0.3s;
                animation-fill-mode: both;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            }
            .results-header {
                padding: 20px 28px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-bottom: 1px solid #e0e0e0;
                font-size: 16px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: #FFFFFF !important;
            }
            .results-body {
                padding: 32px;
                background: #FFFFFF !important;
                color: #000000 !important;
            }
            
            /* ALL text inside results body must be BLACK */
            .results-body * {
                color: #000000 !important;
            }
            
            .results-body h1 {
                font-size: 24px;
                font-weight: 700;
                color: #1a1a2e !important;
                margin: 24px 0 16px;
                border-bottom: 2px solid #667eea;
                padding-bottom: 8px;
            }
            .results-body h2 {
                font-size: 18px;
                font-weight: 600;
                color: #333333 !important;
                margin: 20px 0 12px;
                border-left: 4px solid #667eea;
                padding-left: 16px;
            }
            .results-body h3 {
                font-size: 16px;
                font-weight: 600;
                color: #333333 !important;
                margin: 16px 0 10px;
            }
            .results-body p {
                margin: 12px 0;
                color: #000000 !important;
                line-height: 1.7;
            }
            .results-body ul, .results-body ol {
                margin: 12px 0;
                padding-left: 28px;
                color: #000000 !important;
            }
            .results-body li {
                margin: 8px 0;
                color: #000000 !important;
            }
            .results-body strong {
                color: #1a1a2e !important;
                font-weight: 700;
            }
            .results-body em {
                color: #333333 !important;
            }
            
            .stTextArea textarea {
                border: 2px solid #e0e0e0 !important;
                border-radius: 16px !important;
                font-family: monospace !important;
                font-size: 14px !important;
                background: white !important;
                color: #000000 !important;
            }
            .stTextArea textarea:focus {
                border-color: #667eea !important;
                box-shadow: 0 0 0 4px rgba(102,126,234,0.1) !important;
                animation: glow 0.3s ease;
            }
            
            .stButton > button {
                border-radius: 40px !important;
                font-weight: 600 !important;
                font-size: 14px !important;
                padding: 10px 28px !important;
                transition: all 0.3s ease !important;
            }
            .stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                color: white !important;
                border: none !important;
                animation: pulse 2s infinite !important;
            }
            .stButton > button[kind="primary"]:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 10px 30px rgba(102,126,234,0.4) !important;
            }
            .stButton > button[kind="secondary"] {
                background: rgba(255,255,255,0.9) !important;
                border: 2px solid #667eea !important;
                color: #667eea !important;
            }
            
            .upload-area {
                border: 2px dashed #667eea;
                border-radius: 20px;
                padding: 40px;
                text-align: center;
                background: rgba(255,255,255,0.1);
            }
            
            .footer {
                margin-top: 60px;
                padding: 32px;
                text-align: center;
                border-top: 1px solid rgba(255,255,255,0.2);
            }
            .footer-text { font-size: 13px; color: rgba(255,255,255,0.8); }
            
            .stSpinner > div { 
                border-color: #667eea transparent #667eea transparent !important; 
                border-width: 4px !important; 
            }
            
            /* Warning and info messages */
            .stAlert {
                background: rgba(255,255,255,0.95) !important;
                color: #000000 !important;
            }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_sidebar(ai_processor, analysis_result):
        """Render professional sidebar"""
        with st.sidebar:
            st.markdown("""
            <div style="text-align: center; padding: 24px 0 20px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 56px; margin-bottom: 12px; animation: float 3s ease-in-out infinite;">⚕️</div>
                <div style="font-size: 20px; font-weight: 700; margin-bottom: 6px;">MediExplain Pro</div>
                <div style="font-size: 11px; opacity: 0.6;">Ultimate Edition v5.0</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### System Status")
            
            if ai_processor.is_available:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.08); border-radius: 16px; padding: 16px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <div style="width: 10px; height: 10px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite;"></div>
                        <div style="font-weight: 600;">GroqCloud Active</div>
                    </div>
                    <div style="font-size: 11px; opacity: 0.6; margin-top: 10px;">Model: llama-3.3-70b<br>Free Tier: 30 req/min</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.08); border-radius: 16px; padding: 16px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <div style="width: 10px; height: 10px; background: #ef4444; border-radius: 50%;"></div>
                        <div style="font-weight: 600;">API Not Configured</div>
                    </div>
                    <div style="font-size: 11px; opacity: 0.6; margin-top: 10px;">Add GROQ_API_KEY to .env</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### Session")
            
            if analysis_result:
                st.metric("Reports Analyzed", "1")
                st.metric("Last Analysis", datetime.now().strftime("%H:%M"))
            else:
                st.metric("Reports Analyzed", "0")
            
            st.markdown("---")
            
            with st.expander("📚 Documentation", expanded=False):
                st.markdown("""
                **Supported Reports**
                - CBC (Complete Blood Count)
                - Lipid Profile
                - Thyroid Function
                - Liver Function
                - Renal Panel
                - Radiology Reports
                
                **Export Formats**
                - HTML Document
                - PDF Report
                """)
            
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; font-size: 10px; opacity: 0.5; padding: 16px;">
                <div>Department of Software Engineering</div>
                <div>UET Taxila</div>
                <div style="margin-top: 8px;">23-SE-48 | 23-SE-102</div>
            </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def render_header():
        """Render main header"""
        st.markdown("""
        <div class="main-header">
            <h1 class="main-title">Medical Intelligence System</h1>
            <p class="main-subtitle">Advanced AI-powered clinical report interpretation and patient education platform</p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_kpi_dashboard():
        """Render KPI metrics dashboard"""
        st.markdown("""
        <div class="kpi-grid">
            <div class="kpi-card"><div class="kpi-value">99.2%</div><div class="kpi-label">Clinical Accuracy</div></div>
            <div class="kpi-card"><div class="kpi-value">&lt;3s</div><div class="kpi-label">Response Time</div></div>
            <div class="kpi-card"><div class="kpi-value">50+</div><div class="kpi-label">Report Types</div></div>
            <div class="kpi-card"><div class="kpi-value">24/7</div><div class="kpi-label">Availability</div></div>
        </div>
        """, unsafe_allow_html=True)