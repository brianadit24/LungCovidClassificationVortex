FROM python:3.6.15-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install git
RUN git clone https://github.com/nodefluxio/vortex.git
RUN cd vortex && git checkout drop-enforce && pip install --ignore-installed --timeout=10000 ./src/runtime[onnxruntime]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py" ]