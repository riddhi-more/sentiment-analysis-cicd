"""
Configuration settings for the sentiment analysis project
"""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_RAW_PATH = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
LATEST_MODEL_PATH = MODELS_DIR / "latest_model.pkl"

# Create directories if they don't exist
DATA_RAW_PATH.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Configuration values
MIN_ACCURACY_THRESHOLD = 0.75
MAX_INFERENCE_TIME_MS = 100
LOGGING_LEVEL = "INFO"  
