# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt (if any)
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the Python program
CMD ["python", "minical.py"]
