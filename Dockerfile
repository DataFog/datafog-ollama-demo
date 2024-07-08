# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    procps \
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
RUN echo '#!/bin/bash\n\
export OLLAMA_HOST=0.0.0.0:11434\n\
export OLLAMA_MODELS=/app/models\n\
mkdir -p $OLLAMA_MODELS\n\
ollama serve &\n\
sleep 10\n\
ollama pull phi3\n\
while ! ollama list | grep -q phi3; do\n\
    echo "Waiting for phi3 model to be available..."\n\
    sleep 5\n\
done\n\
echo "Ollama and phi3 model are ready. Starting Streamlit..."\n\
streamlit run app.py' > /app/start.sh

RUN chmod +x /app/start.sh

# Run the script when the container launches
CMD ["/app/start.sh"]