FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git

RUN pip3 install pyyaml

COPY feed.py /user/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

entrypoint ["/entrypoint.sh"]
