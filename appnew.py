from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import openai
import replicate
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure API tokens
replicate.api_token = os.getenv('REPLICATE_API_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
openai.api_key = openai_api_key

def generate_lyrics(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "you are a music lyrics writer and your task is to write lyrics of music under 30 words based on users's prompt. just return lyrics nothing else."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        output = response['choices'][0]['message']['content']
        cleaned_output = output.replace("\n", " ")
        formatted_lyrics = f"♪ {cleaned_output} ♪"
        return formatted_lyrics
    except Exception as e:
        print(f"Error generating lyrics: {e}")
        return "♪ ♪"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-music", methods=["POST"])
def generate_music():
    try:
        prompt = request.form["prompt"]
        duration = request.form["duration"]
        lyrics = generate_lyrics(prompt)
        prompt_with_lyrics = lyrics
        print(prompt_with_lyrics)

        output = replicate.run(
            "suno-ai/bark:b76242b40d67c76ab6742e987628a2a9ac019e11d56ab96c4e91ce03b79b2787",
            input={
                "prompt": prompt_with_lyrics,
                "text_temp": 0.7,
                "output_full": False,
                "waveform_temp": 0.7
            }
        )
        print(output)
        
        if 'audio_out' in output:
            music_url = output['audio_out']
            return jsonify({"url": music_url})
        else:
            return jsonify({"error": "Audio generation failed"}), 500
    except Exception as e:
        print(f"Error generating music: {e}")
        return jsonify({"error": "Failed to generate music"}), 500

if __name__ == "__main__":
    app.run(debug=True)
