# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies needed for Pygame and audio processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libglib2.0-0 \
    libsdl2-mixer-2.0-0 \
    alsa-utils \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the necessary port (if applicable)
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]
