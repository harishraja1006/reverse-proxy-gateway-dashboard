# ==========================================================
# Reverse Proxy Gateway Docker Image
# ==========================================================

# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy Requirements
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Expose Application Port
EXPOSE 8000

# Start Application
CMD ["python", "-m", "loadbalancer.app"]
