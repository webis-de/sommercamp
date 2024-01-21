FROM mcr.microsoft.com/devcontainers/base:ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.11 python3.11-dev python3.11-venv git build-essential zlib1g-dev protobuf-compiler
RUN ([ -d /venv ] || python3.11 -m venv /venv) && /venv/bin/pip install --upgrade pip
WORKDIR /workspace/
ADD pyproject.toml pyproject.toml
ARG PSEUDO_VERSION=1
RUN SETUPTOOLS_SCM_PRETEND_VERSION=${PSEUDO_VERSION} /venv/bin/pip install -e .
ADD .git .git
RUN /venv/bin/pip install -e .
