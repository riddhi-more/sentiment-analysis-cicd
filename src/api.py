"""
FastAPI server for sentiment analysis
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.model import SentimentModel
from src.config import LATEST_MODEL_PATH
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Global variable to store model
model = None

@app.on_event("startup")
async def startup_event():
    """Load model when server starts"""
    global model
    try:
        model = SentimentModel()
        model.load(str(LATEST_MODEL_PATH))
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

# Request model - what user sends
class PredictionRequest(BaseModel):
    text: str

# Response model - what we send back
class PredictionResponse(BaseModel):
    text: str
    sentiment: str

# Health check endpoint
@app.get("/health")
async def health():
    """Health check endpoint for Kubernetes"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Predict sentiment of input text
    
    Args:
        text: Input text to classify
    
    Returns:
        Sentiment prediction (positive, negative, neutral)
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    if not request.text or len(request.text) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        sentiment = model.predict(request.text)
        return PredictionResponse(text=request.text, sentiment=sentiment)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - shows available endpoints"""
    return {
        "message": "Sentiment Analysis API",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "docs": "/docs"
        }
    }
