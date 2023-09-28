#use the official python image as base image

FROM python:3.8-slim





#set the working directory in the container

WORKDIR /testwork



#copy the current directory contents into the container 

COPY server.py /testwork/

COPY config.json /testwork/



EXPOSE 6000



#run the python script when the container launches

ENTRYPOINT ["python3","server.py"]
