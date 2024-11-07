"""
Main package for the log analysis project.
"""

from .main import run_analysis
from .config import Config

__all__ = [
    "run_analysis",
    "Config"
]