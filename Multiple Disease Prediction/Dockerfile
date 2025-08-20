#This sets up the container with python 3.10 installed.
FROM python:3.10-slim

#This copies everything in your current directory to the /app directory in the container.
COPY . /app

#This sets the working directory to /app
WORKDIR /app

# Install system dependencies for building numpy and other packages
RUN apt-get update && apt-get install -y build-essential gcc

#This installs the required packages
RUN pip install -r requirements.txt

#this tells docker to listen on port 80
EXPOSE 8501

#this creates a .streamlit directory in the root of the container
RUN mkdir -p /.streamlit

RUN cp config.toml /.streamlit/config.toml

RUN cp credentials.toml /.streamlit/credentials.toml

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "app.py" ]