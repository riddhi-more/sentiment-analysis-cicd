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

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Default command: Run tests
CMD ["pytest", "tests/", "-v"]
