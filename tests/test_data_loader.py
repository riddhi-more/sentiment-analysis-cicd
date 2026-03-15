"""
Tests for data loading module
"""

import pytest
from src.data_loader import get_sample_data

def test_get_sample_data():
    """Test that sample data loads correctly"""
    texts, labels = get_sample_data()
    
    assert len(texts) == 5
    assert len(labels) == 5
    assert len(texts) == len(labels)

def test_sample_data_content():
    """Test that sample data has valid content"""
    texts, labels = get_sample_data()
    
    # Check all texts are strings
    assert all(isinstance(t, str) for t in texts)
    
    # Check all labels are strings
    assert all(isinstance(l, str) for l in labels)
    
    # Check labels are valid sentiments
    valid_labels = ["positive", "negative", "neutral"]
    assert all(l in valid_labels for l in labels)

def test_sample_data_not_empty():
    """Test that sample data is not empty"""
    texts, labels = get_sample_data()
    
    assert len(texts) > 0
    assert len(labels) > 0
    assert all(len(t) > 0 for t in texts)
