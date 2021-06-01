# Built from https://github.com/grammatek/g2p-thrax.git
FROM g2p-thrax

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN apk add --no-cache git
RUN apk add --no-cache make
RUN apk add --no-cache cmake
RUN git clone https://github.com/grammatek/g2p-thrax.git

WORKDIR /usr/src/app/g2p-thrax/
RUN mkdir build && cd build && cmake .. && make

COPY main.py .


EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
