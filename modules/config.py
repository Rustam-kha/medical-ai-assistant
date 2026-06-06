"""
Configuration Module - Enterprise Settings
Author: Mubashir Ahmad Ameer, Rustam Khan
"""

import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional

load_dotenv()


@dataclass
class Config:
    """Enterprise configuration settings"""
    
    # API Configuration
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    API_TIMEOUT: int = 60
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.3
    
    # Application Settings
    APP_NAME: str = "MediExplain Pro"
    APP_VERSION: str = "5.0.0"
    APP_DESCRIPTION: str = "Enterprise Medical Intelligence System"
    
    # File Settings
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10 MB
    
    # Rate Limits
    FREE_TIER_REQUESTS_PER_MINUTE: int = 30
    
    @property
    def is_api_configured(self) -> bool:
        return bool(self.GROQ_API_KEY)


# Global configuration instance
config = Config()