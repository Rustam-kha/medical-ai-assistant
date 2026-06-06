"""
PDF Processor Module - Text Extraction from Clinical Documents
Author: Mubashir Ahmad Ameer, Rustam Khan
"""

from PyPDF2 import PdfReader
from modules.config import config


class PDFProcessor:
    """Handles PDF text extraction for medical reports"""
    
    @staticmethod
    def extract_text(pdf_file) -> str:
        """Extract text from uploaded PDF file"""
        try:
            pdf_reader = PdfReader(pdf_file)
            text_pages = []
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                extracted = page.extract_text()
                if extracted and extracted.strip():
                    text_pages.append(f"[Page {page_num}]\n{extracted.strip()}")
            
            if not text_pages:
                return None
            
            return "\n\n".join(text_pages)
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def validate_pdf(file) -> tuple:
        """Validate PDF file size and format"""
        if file.size > config.MAX_FILE_SIZE:
            return False, f"File size exceeds {config.MAX_FILE_SIZE // (1024*1024)} MB limit"
        return True, "OK"
    
    @staticmethod
    def get_preview(text: str, max_length: int = 500) -> str:
        """Generate preview of extracted text"""
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text