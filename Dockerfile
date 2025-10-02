# Use a stable Debian-based Python + NodeJS image
FROM nikolaik/python-nodejs:python3.10-nodejs19-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies
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

# Copy project files
COPY . /app/

# Upgrade pip and install Python requirements
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Environment variable for NodeJS
ENV NODE_OPTIONS=--openssl-legacy-provider

# Start the bot
CMD ["bash", "start"]
