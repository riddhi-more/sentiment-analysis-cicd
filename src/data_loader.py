"""
Data loading and preprocessing module
Handles loading CSV data and preparing it for ML
"""

import pandas as pd
from pathlib import Path
from src.config import DATA_RAW_PATH

def load_data(file_path):
    """
    Load data from CSV file
    
    Args:
        file_path: Path to CSV file
    
    Returns:
        DataFrame with data
    """
    df = pd.read_csv(file_path)
    return df

def get_sample_data():
    """
    Create sample training data for testing
    
    Returns:
        Tuple of (texts, labels)
    """
    texts = [
        "I love this product!",
        "This is terrible",
        "It's okay",
        "Amazing service",
        "Very disappointed"
    ]
    labels = [
        "positive",
        "negative",
        "neutral",
        "positive",
        "negative"
    ]
    return texts, labels