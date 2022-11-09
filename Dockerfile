FROM python:3.9-buster

RUN pip3 install pipenv

RUN apt-get -y update
RUN apt-get -y install git

RUN mkdir /opt/app 
WORKDIR /opt/app
COPY Pipfile ./
RUN pipenv install --skip-lock
COPY . .

RUN echo "Build commit: $BUILD_COMMIT" > /opt/app/build.info && echo "Build time: $BUILD_TIME" >> /opt/app/build.info
ENV PYTHONPATH "${PYTHONPATH}:/opt/app"
ENV GIT_PYTHON_GIT_EXECUTABLE /usr/bin/git

CMD pipenv run python main.py
