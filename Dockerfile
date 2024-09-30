FROM ubuntu:latest

# Install required packages and pip dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    build-essential \
    libyaml-dev \
    && python3 -m pip install --upgrade pip setuptools wheel

# Install PyYAML with no cache to prevent any issues with caching
RUN pip3 install --no-cache-dir PyYAML

COPY feed.py /user/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

entrypoint ["/entrypoint.sh"]
