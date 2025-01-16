# indicate that the container is based on the "python:3.12-slim-bookworm" image available in Docker Hub (this is why there is no url)
# List of available prebuilt image are available here : https://hub.docker.com/
# You can find this image by searchig "python" in the search bar
# This version is a debian slim version (light version without to many pre installed tools) with python 3.12 installed
FROM python:3.12-slim-bookworm

# Add Environment variable in the container. This one is used by airflow installation
# /!\ WARNING /!\  Update this path to match your project folder name  /!\ WARNING /!\
ENV AIRFLOW_HOME='/workspaces/min-test-devcontainer/airflow'

# Create and change directory for command in the dockerfile
WORKDIR /app

# Copy the current folder (here the folder containing the requirements.txt file and .devcontainer folder) into the devcontainer
# This is done to be able to use the requirements.txt in the devcontainer
COPY . .

# RUN let us run command as if we were in a terminal.
RUN apt-get update -y \
  # install git with minimal elements to be able to commit and push inside the container
  && apt-get install -y --no-install-recommends git \
  # upgrade pip to be up-to-date
  && pip install --upgrade pip \
  # install the liste of library in the requirements.txt file
  && pip install -r requirements.txt \
  # install airflow
  && chmod +x install_airflow.sh \
  && ./install_airflow.sh
  

# When everything is done, this command is run if we run the container.
# In devcontainer, this CMD is not used and we can interact with files inside the container
# When our scripts are ready to be run, we need to adapt this command to bu runnable when running the container in production
CMD python main.py

EXPOSE 8080