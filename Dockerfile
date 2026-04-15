FROM python:3.10-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg nodejs npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN pip3 install --no-cache-dir -e .

CMD bash start
