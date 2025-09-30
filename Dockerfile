# Use an official Python 3.10 image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose FastAPI port
EXPOSE 5000

# Run the FastAPI app
CMD ["python", "app.py"]
