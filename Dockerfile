# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY src/ ./src/
COPY tests/ ./tests/
COPY models/ ./models/

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run the API server (not tests)
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
