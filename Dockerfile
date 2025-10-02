FROM nikolaik/python-nodejs:python3.10-nodejs19-bullseye
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
