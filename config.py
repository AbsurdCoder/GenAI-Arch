"""
Configuration settings for the log analysis project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration settings for the log analysis project.
    """

    # Paths and directories
    LOG_DIR = 'logs' # os.getenv('LOG_DIR', 'logs/')
    # EMBEDDING_CACHE_DIR = os.getenv('EMBEDDING_CACHE_DIR', 'cache/embeddings/')
    # REPORT_OUTPUT_PATH = os.getenv('REPORT_OUTPUT_PATH', 'reports/analysis_report.pdf')

    # # OpenAI API
    # OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # # Model settings
    # TEXT_CLASSIFICATION_NUM_CLASSES = int(os.getenv('TEXT_CLASSIFICATION_NUM_CLASSES', 5))
    # ANOMALY_DETECTION_CONTAMINATION = float(os.getenv('ANOMALY_DETECTION_CONTAMINATION', 0.01))

    # Other settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')