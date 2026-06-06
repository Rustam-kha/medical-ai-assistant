"""
MediExplain Pro - Enterprise Medical Intelligence System
Authors: Mubashir Ahmad Ameer (23-SE-48), Rustam Khan (23-SE-102)
UET Taxila - Artificial Intelligence Semester Project
Version: 5.1 - Fixed White Background
"""

import streamlit as st
import time
from datetime import datetime

# Import modules
from modules.config import config
from modules.ai_processor import AIProcessor
from modules.pdf_processor import PDFProcessor
from modules.report_generator import ReportGenerator
from modules.ui_components import UIComponents


def initialize_session_state():
    """Initialize all session state variables"""
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'report_text' not in st.session_state:
        st.session_state.report_text = ""


def render_input_section(pdf_processor):
    """Render the data ingestion section with tabs"""
    st.markdown("""
    <div class="input-card">
        <div class="input-card-header">Data Ingestion</div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📝 Text Input", "📄 PDF Upload"])
    
    with tab1:
        report_input = st.text_area(
            "",
            height=280,
            key="text_input_area",
            placeholder="Paste your medical report text here...\n\nExample:\nPatient: 45-year-old male\n\nComplete Blood Count Results:\nHemoglobin: 10.2 g/dL (Reference: 13.5-17.5 g/dL) [LOW]\nWhite Blood Cells: 7,500 /uL (Reference: 4,500-11,000 /uL) [NORMAL]\nPlatelets: 180,000 /uL (Reference: 150,000-450,000 /uL) [NORMAL]",
            label_visibility="collapsed"
        )
        
        if report_input != st.session_state.report_text:
            st.session_state.report_text = report_input
            if st.session_state.analysis_result:
                st.session_state.analysis_result = None
    
    with tab2:
        st.markdown('<div class="upload-area">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Clinical Document", type=['pdf'], 
                                          label_visibility="collapsed", key="pdf_uploader")
        st.markdown('<div style="font-size: 12px; color: #666; margin-top: 12px; text-align: center;">Supported: PDF files up to 10 MB</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if uploaded_file:
            is_valid, message = pdf_processor.validate_pdf(uploaded_file)
            if is_valid:
                with st.spinner("Processing PDF document..."):
                    extracted_text = pdf_processor.extract_text(uploaded_file)
                    if extracted_text and not extracted_text.startswith("Error"):
                        st.session_state.report_text = extracted_text
                        if st.session_state.analysis_result:
                            st.session_state.analysis_result = None
                        st.success("✓ Document processed successfully")
                        with st.expander("Preview Extracted Content"):
                            preview = extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text
                            st.text(preview)
                    else:
                        st.error(extracted_text if extracted_text else "Failed to extract text from PDF")
            else:
                st.error(message)
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_action_buttons():
    """Render action buttons"""
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if st.button("Clear Fields", type="secondary", use_container_width=True):
            st.session_state.report_text = ""
            st.session_state.analysis_result = None
            st.rerun()
    
    with col2:
        if st.button("Copy Text", type="secondary", use_container_width=True):
            if st.session_state.report_text:
                st.success("✓ Text ready to copy")
    
    with col3:
        return st.button("Analyze Report", type="primary", use_container_width=True)


def render_analysis_result(analysis_result):
    """Render the analysis result with SOLID WHITE background and BLACK text"""
    if analysis_result:
        # Escape the content for safe HTML rendering while preserving formatting
        import html
        
        # Convert markdown-style formatting to HTML for better display
        content = analysis_result
        
        # Preserve line breaks and basic formatting
        content = content.replace('\n', '<br>')
        
        # Convert markdown headers
        import re
        content = re.sub(r'### (.*?)(<br>|$)', r'<h3 style="color:#333; margin-top:20px; margin-bottom:10px;">\1</h3>', content)
        content = re.sub(r'## (.*?)(<br>|$)', r'<h2 style="color:#222; margin-top:25px; margin-bottom:12px; border-left:4px solid #667eea; padding-left:15px;">\1</h2>', content)
        content = re.sub(r'# (.*?)(<br>|$)', r'<h1 style="color:#1a1a2e; margin-top:30px; margin-bottom:15px; border-bottom:2px solid #667eea; padding-bottom:8px;">\1</h1>', content)
        
        # Convert bullet points
        content = re.sub(r'• (.*?)(<br>|$)', r'<li style="margin:5px 0; color:#000;">\1</li>', content)
        content = re.sub(r'<li>', '<ul style="margin:10px 0; padding-left:25px;"><li>', content)
        content = re.sub(r'(</li>)(?!.*<li>)', r'</li></ul>', content)
        
        # Convert numbered lists
        content = re.sub(r'(\d+)\. (.*?)(<br>|$)', r'<li style="margin:5px 0; color:#000;">\2</li>', content)
        
        # Make strong/bold text
        content = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color:#1a1a2e; font-weight:700;">\1</strong>', content)
        
        # Make italic text
        content = re.sub(r'\*(.*?)\*', r'<em style="color:#555;">\1</em>', content)
        
        st.markdown(f"""
        <div style="background: #FFFFFF; border-radius: 24px; border: 1px solid #e0e0e0; 
                    margin-top: 28px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
            <div style="padding: 20px 28px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-bottom: 1px solid #e0e0e0; font-size: 16px; font-weight: 700; 
                        text-transform: uppercase; letter-spacing: 1px; color: #FFFFFF;">
                Analysis Results
            </div>
            <div style="padding: 32px; background: #FFFFFF; color: #000000; font-size: 15px; line-height: 1.8;">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Export Options
        st.markdown("### Export Options")
        col_export1, col_export2 = st.columns(2)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        with col_export1:
            html_content = ReportGenerator.generate_html_report(analysis_result)
            b64 = ReportGenerator.get_html_download_link(analysis_result, f"report_{timestamp}")
            st.markdown(f"""
            <div style="text-align: center;">
                <a href="{b64}" download="clinical_report_{timestamp}.html"
                   style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; 
                          padding: 12px 24px; border-radius: 40px; text-decoration: none; 
                          display: inline-block; font-weight: 600; transition: all 0.3s ease;">
                    Export HTML Document
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col_export2:
            pdf_buffer = ReportGenerator.generate_pdf_report(analysis_result)
            st.download_button(
                label="Export PDF Document",
                data=pdf_buffer,
                file_name=f"clinical_report_{timestamp}.pdf",
                mime="application/pdf",
                use_container_width=True
            )


def render_footer():
    """Render professional footer"""
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 24px; margin-top: 32px; border-left: 4px solid #667eea;">
        <div style="font-size: 14px; font-weight: 700; color: #667eea; margin-bottom: 12px;">Medical Disclaimer</div>
        <div style="font-size: 13px; color: #333; line-height: 1.6;">
            MediExplain Pro is an educational artificial intelligence system designed to help patients understand their medical reports. 
            This system does not provide medical advice, diagnosis, or treatment recommendations. 
            Always consult with licensed healthcare professionals for clinical decision-making.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer">
        <div class="footer-text">MediExplain Pro Ultimate Edition | Powered by GroqCloud</div>
        <div class="footer-text" style="margin-top: 8px; font-size: 11px;">Department of Software Engineering | University of Engineering & Technology, Taxila</div>
        <div class="footer-text" style="margin-top: 6px; font-size: 10px;">Mubashir Ahmad Ameer (23-SE-48) | Rustam Khan (23-SE-102)</div>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application entry point"""
    
    st.set_page_config(
        page_title=f"{config.APP_NAME} | Clinical Intelligence Platform",
        page_icon="⚕️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize
    initialize_session_state()
    ui = UIComponents()
    pdf_processor = PDFProcessor()
    ai_processor = AIProcessor()
    
    # Inject CSS
    ui.inject_css()
    
    # Render Sidebar
    ui.render_sidebar(ai_processor, st.session_state.analysis_result)
    
    # Main content container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Render Header
    ui.render_header()
    
    # Render KPI Dashboard
    ui.render_kpi_dashboard()
    
    # Render Input Section
    render_input_section(pdf_processor)
    
    # Render Action Buttons
    analyze_button = render_action_buttons()
    
    # Process Analysis
    if analyze_button:
        if not st.session_state.report_text:
            st.warning("Please provide a medical report for analysis. Paste text or upload a PDF.")
        elif not ai_processor.is_available:
            st.error("GroqCloud API not configured. Please add GROQ_API_KEY to your .env file.")
        elif len(st.session_state.report_text.strip()) < 20:
            st.warning("Please provide a more detailed medical report. At least 20 characters required.")
        else:
            with st.spinner("Analyzing clinical data with AI..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.008)
                    progress_bar.progress(i + 1)
                progress_bar.empty()
                
                result = ai_processor.analyze_medical_report(st.session_state.report_text)
                st.session_state.analysis_result = result
    
    # Render Analysis Result (with SOLID WHITE background and BLACK text)
    render_analysis_result(st.session_state.analysis_result)
    
    # Render Footer
    render_footer()
    
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()