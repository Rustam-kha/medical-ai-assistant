"""
AI Processor Module - GroqCloud API Integration
Author: Mubashir Ahmad Ameer, Rustam Khan
"""

import streamlit as st
from groq import Groq
from modules.config import config
from modules.constants import SYSTEM_PROMPT


class AIProcessor:
    """Handles GroqCloud API interactions for medical analysis"""
    
    def __init__(self):
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Groq client if API key is available"""
        if config.GROQ_API_KEY:
            try:
                self.client = Groq(api_key=config.GROQ_API_KEY)
            except Exception:
                self.client = None
    
    def analyze_medical_report(self, report_text: str) -> str:
        """Process medical report using GroqCloud API"""
        if not self.client:
            return self._get_api_error_message()
        
        if not report_text or len(report_text.strip()) < 20:
            return self._get_insufficient_data_message()
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"MEDICAL REPORT:\n{report_text}"}
                ],
                model=config.GROQ_MODEL,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS,
                timeout=config.API_TIMEOUT
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return self._handle_api_error(e)
    
    def _get_api_error_message(self) -> str:
        return """## Configuration Error

GroqCloud API key not configured. Please add your API key to the `.env` file.

**Get your free API key:**
1. Visit https://console.groq.com/keys
2. Sign up with your email (no credit card required)
3. Copy your API key starting with `gsk_`
4. Add to `.env` file: `GROQ_API_KEY=your_key_here`"""
    
    def _get_insufficient_data_message(self) -> str:
        return """## Insufficient Data

Please provide a complete medical report with:
- Patient information
- Test results with reference ranges
- Clinical findings or impressions

**Example format:** 
Hemoglobin: 10.2 g/dL (Reference: 13.5-17.5) [LOW]"""
    
    def _handle_api_error(self, error: Exception) -> str:
        error_msg = str(error).lower()
        if "rate_limit" in error_msg or "429" in error_msg:
            return """## Rate Limit Exceeded

The free tier allows 30 requests per minute. Please wait a moment before trying again."""
        elif "api_key" in error_msg or "unauthorized" in error_msg:
            return """## Authentication Failed

Your GroqCloud API key appears to be invalid. Please verify your API key in the `.env` file."""
        else:
            return f"## Processing Error\n\n{str(error)[:300]}"
    
    @property
    def is_available(self) -> bool:
        return self.client is not None and config.GROQ_API_KEY is not None