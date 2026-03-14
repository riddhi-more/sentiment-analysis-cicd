"""
Training script for sentiment analysis model
Trains the model on sample data
"""

from src.data_loader import get_sample_data
from src.model import SentimentModel
from src.config import LATEST_MODEL_PATH

def train_model():
    """
    Train sentiment analysis model
    
    Returns:
        Trained model object
    """
    print("Loading data...")
    texts, labels = get_sample_data()
    
    print("Creating model...")
    model = SentimentModel()
    
    print("Training model...")
    model.train(texts, labels)
    
    print("Testing predictions...")
    test_texts = [
        "I love this!",
        "This is bad",
        "It's okay"
    ]
    
    for text in test_texts:
        prediction = model.predict(text)
        print(f"Text: '{text}' → Prediction: {prediction}")
    
    print(f"Saving model to {LATEST_MODEL_PATH}...")
    model.save(str(LATEST_MODEL_PATH))
    
    print("✅ Training complete!")
    return model

if __name__ == "__main__":
    train_model()
