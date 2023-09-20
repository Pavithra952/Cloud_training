# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Python script and the config file into the container
COPY client.py config_file.json /app/

# Install any needed packages specified in requirements.txt (if any)
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the Python script
CMD ["python", "customer1.py"]
