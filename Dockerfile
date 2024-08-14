# Official Python runtime as base image
FROM python:3.9

# Set working directory in container
WORKDIR /app

# Copy requirements file to working directory
COPY requirements.txt .

# Install Python dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code to working directory
COPY . .

# Expose port on which application will run
EXPOSE 8000

# Run application using Python
CMD ["python", "main.py"]