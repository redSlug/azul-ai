import json
import os

from openai import OpenAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/move", methods=["POST"])
def move():
    state = request.get_json()
    print("validated user input=", state)
    prompt = f"""Analyze this Azul board game state and recommend the best possible move.
    Current game state: {json.dumps(state)}
    Consider the current game state including source factories and target rows.
    
    Return response in raw JSON format only with the following fields:
    {{
            "source_factory_index": number,
            "source_tile_index": number,
            "source_tile_color": string,
            "source_tile_count": number,
            "target_row": number,
            "target_open_space_count": number,
    }}
    Only return the JSON not formatted as a code block
    """

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert Azul board game strategist. Analyze the game state and recommend the optimal move.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=500,
    )
    print("response", response)
    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(port=8000, debug=True)
