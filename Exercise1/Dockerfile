# Use an official Python runtime as a parent image
FROM python:3.8-slim
ENV FLASK_APP Restapi_flask.py
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Restapi_flask.py /app

# Make port 5000 available to the world outside this container
RUN pip install Flask

EXPOSE 5000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "Restapi_flask.py"]

