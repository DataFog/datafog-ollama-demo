# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl https://ollama.ai/install.sh | sh

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501 11434

# Create a script to run both Ollama and Streamlit
RUN echo '#!/bin/bash\nollama serve &\nstreamlit run app.py' > /app/start.sh
RUN chmod +x /app/start.sh

# Run the script when the container launches
CMD ["/app/start.sh"]