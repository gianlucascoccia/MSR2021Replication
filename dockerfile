FROM ubuntu:20.04


ENV DATASET_PATH=./so_questions.csv
ENV OUTPUT_PATH=./notebook/output
ENV TOPICS_NUM=15

RUN apt update -y
RUN apt install -y python3-pip libpq-dev python-dev

COPY notebook/requirements.txt /requirements.txt
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt
RUN pip3 install jupyterlab


COPY notebook /notebook
COPY mallet /mallet

WORKDIR /notebook
CMD jupyter-lab --ip='*' --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.password=''