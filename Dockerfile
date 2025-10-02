# Use a modern Python + NodeJS image with Debian Bullseye
FROM nikolaik/python-nodejs:python3.11-nodejs22-bullseye

# Set working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ffmpeg \
       git \
       curl \
       wget \
       build-essential \
       python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files
COPY . /app/

# Upgrade pip & install dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Environment variable for NodeJS crypto compatibility
ENV NODE_OPTIONS=--openssl-legacy-provider

# Start your bot (change if you use another start command)
CMD ["bash", "start"]
