FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Base image may include an outdated Yarn apt source that breaks apt-get update.
RUN rm -f /etc/apt/sources.list.d/yarn.list

RUN apt-get update \
    && apt-get install -y --no-install-recommends sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
