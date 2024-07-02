# datafog-ollama-demo

This repository contains a demonstration of the DataFog Instructor SDK using Ollama and Streamlit. It showcases the named entity recognition (NER) capabilities of the SDK in an interactive web application.

## Prerequisites

- Python 3.10 or higher
- Docker (optional, for Docker-based setup)
- Ollama (required for non-Docker setup)

## Setup and Running (Docker)

1. Clone this repository:
   ```
   git clone https://github.com/datafog/datafog-instructor/datafog-ollama-demo.git
   cd datafog-ollama-demo
   ```

2. Build the Docker image:
   ```
   docker build -t datafog-demo .
   ```

3. Run the Docker container:
   ```
   docker run -p 8501:8501 datafog-demo
   ```

4. Open your web browser and navigate to `http://localhost:8501` to access the demo.

## Setup and Running (Without Docker)

1. Clone this repository:
   ```
   git clone https://github.com/datafog/datafog-instructor/datafog-ollama-demo.git
   cd datafog-ollama-demo
   ```

2. Install Ollama by following the instructions at [https://ollama.ai/](https://ollama.ai/)

3. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Start the Ollama server:
   ```
   ollama serve
   ```

6. In a new terminal window, start the Streamlit app:
   ```
   streamlit run app.py
   ```

7. Open your web browser and navigate to `http://localhost:8501` to access the demo.

## Usage

Once the application is running:

1. Enter text in the provided input field.
2. Click the "Detect Entities" button.
3. View the detected entities and their types in the results section.

## Customization

You can customize the entity types and models used by modifying the `app.py` file. Refer to the [DataFog Instructor SDK documentation](https://github.com/datafog/datafog-instructor/datafog-instructor) for more details on available options.

## Troubleshooting

- If you encounter any issues with Ollama, ensure it's properly installed and the server is running.
- For Docker-related issues, make sure Docker is installed and running on your system.
- If you face any problems with the Streamlit app, check the console output for error messages.

## Contributing

Contributions to improve the demo are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have questions, please open an issue in this repository or contact support@datafog.ai.

## Links

- [DataFog Website](https://datafog.ai)
- [DataFog Instructor SDK](https://github.com/datafog/datafog-instructor/datafog-instructor)
- [Ollama](https://ollama.ai/)
- [Streamlit](https://streamlit.io/)