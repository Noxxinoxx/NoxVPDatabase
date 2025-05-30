# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
#COPY Server/requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

# Copy your server code into the container
COPY Server/ ./Server/

# Copy an empty Database folder just to ensure it exists (won't overwrite host bind mount)
RUN mkdir -p /app/Database

# Set working directory to your server code folder
WORKDIR /app/Server

# Run the main server script when container starts
CMD ["python", "main.py"]
