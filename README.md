# Music Generator Flask App

This is a Flask application that generates music lyrics and audio based on user prompts. The app uses OpenAI's GPT-3.5-turbo for lyrics generation and Replicate's Suno-AI Bark model for audio generation.

## Features

- Generate music lyrics based on user input prompts.
- Convert generated lyrics into audio.
- Return a URL to the generated audio file.

## Requirements

- Python 3.7+
- Flask
- python-dotenv
- OpenAI API key
- Replicate API token

## Setup

1. Clone the repository:
    ```bash
    cd music-generator-flask-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your API keys:
    ```env
    REPLICATE_API_TOKEN=your_replicate_api_token
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Flask app:
    ```bash
    flask run
    ```

## Usage

1. Open a web browser and go to `http://127.0.0.1:5000/`.
2. Enter a prompt for the music lyrics and the desired duration of the music.
3. Click the "Generate" button to create the lyrics and audio.
4. The generated audio will be displayed as a URL that you can click to listen to the music.

## File Structure

