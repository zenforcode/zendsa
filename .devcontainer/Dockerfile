# Start from a base image with Python 3.11
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install required OS packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        build-essential \
        curl \
        unzip \
        zip \
        openjdk-17-jdk \
        clang \
        g++ \
        cmake \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Set default user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN usermod -aG sudo ${USERNAME}

# Make sure all tools are on the PATH
ENV CARGO_HOME=/root/.cargo

