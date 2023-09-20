# Use an official Python runtime as a parent image

RUN pip install xmltodict

# Set the working directory in the container
WORKDIR /testwork

copy pavithra.xml /testwork/

# Copy the Python script to the container
COPY server.py /testwork/

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/server.py"]
                                                                                                                                                                                                                                          ~                                                                                                                                               
