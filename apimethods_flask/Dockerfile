# Stage 1: Build the Flask application
FROM python:3.8-slim AS builder

WORKDIR /app

# Copy the application files to the container
COPY requirements.txt .
COPY app.py .
COPY Database_operations.py .
COPY Flaskapimethods.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the SQLite database
FROM builder AS database-creator

# Create the SQLite database and initialize it
RUN python Database_operations.py

# Stage 3: Final production image
FROM python:3.8-slim

WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app/app.py .
COPY --from=builder /app/Flaskapimethods.py .

# Expose the port that your Flask application listens on
EXPOSE 5000

# Command to start the Flask application
CMD ["python", "Flaskapimethods.py"]
