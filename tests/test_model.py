"""
Tests for the sentiment analysis model
"""

import pytest
from src.model import SentimentModel

def test_model_creation():
    """Test that model can be created"""
    model = SentimentModel()
    assert model is not None
    assert model.is_trained == False

def test_model_training():
    """Test that model can be trained"""
    model = SentimentModel()
    
    texts = ["I love this", "I hate this", "It's okay"]
    labels = ["positive", "negative", "neutral"]
    
    model.train(texts, labels)
    assert model.is_trained == True

def test_model_prediction():
    """Test that model can make predictions"""
    model = SentimentModel()
    
    texts = ["I love this", "I hate this", "It's okay"]
    labels = ["positive", "negative", "neutral"]
    
    model.train(texts, labels)
    
    prediction = model.predict("I love this!")
    assert prediction in ["positive", "negative", "neutral"]

def test_model_requires_training():
    """Test that prediction fails without training"""
    model = SentimentModel()
    
    with pytest.raises(ValueError):
        model.predict("Some text")