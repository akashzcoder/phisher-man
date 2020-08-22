FROM continuumio/miniconda3:4.5.4

ENV CODE /code

WORKDIR $CODE

# Install tools
RUN apt-get update && apt-get install -y  \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    make \
    python \
    python-dev \
    git \
    libssl-dev \
    libffi-dev \
    python-pip \
    bzip2

# Get Docker repo key
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Add Docker repo
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

# Install Docker
RUN apt-get update && apt-get -y install docker-ce

# Update conda
RUN conda install conda==4.5.8

# Create environment using file
COPY environment.yml $CODE
RUN pip install django
RUN pip install djangorestframework

COPY ./machinelearning $CODE
COPY ./backend $CODE

RUN conda env update -f environment.yml -n root

# run the django server
WORKDIR $CODE/backend/phish_manager
RUN python manage.py makemigrations phisherman
RUN python manage.py migrate
RUN python manage.py runserver
