# Use the official Python slim image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (needed for some Python packages)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies, including uvicorn
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt uvicorn

# Copy the rest of the app
COPY . .

# Expose the FastAPI port
EXPOSE 8080

# Run the application explicitly using Python
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
