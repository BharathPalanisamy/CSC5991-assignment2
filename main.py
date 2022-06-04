from flask import Flask, jsonify, request
import random
import json
app = Flask(__name__)
@app.route('/jokes/', methods=['GET', 'POST'])

def joke():
    num = request.args.get('num', type=int)
    jokes = [
        "What do you call a sleeping bull? A bulldozer.",
        "Why do melons have weddings? They cantaloupe..",
        "How do you make a tissue dance? You put a little boogie in it.",
        "Why did the photo go to jail? It was framed.",
        "Why did the golfer bring an extra pair of pants? In case he got a hole in one.",
        "Why did the baby strawberry cry? His parents were in a jam.",
        "Why did the scarecrow win an award? He was outstanding in his field.",
        "What kind of jewelry do rabbits wear? 14 carrot gold.",
        "Where do polar bears keep their money? In a snowbank.",
        "What do you call a factory that makes okay products? A satis-factory."
    ]

    return jsonify(
        jokes = random.sample(jokes,k=num)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)