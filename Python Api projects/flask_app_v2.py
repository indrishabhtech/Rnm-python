import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Function to read data from the JSON file
def read_json_file():
    with open('dummy.json') as f:
        data = json.load(f)
    return data

# Route to retrieve all words from the JSON file
@app.route('/words', methods=['GET'])
def get_words():
    data = read_json_file()
    words = data['words']
    return jsonify(words)

# Route to add a new word with its synonyms
@app.route('/words/add', methods=['POST'])
def add_word():
    data = read_json_file()
    new_word = {}
    new_word['word'] = input("Enter the word: ")
    new_word['synonym'] = input("Enter the synonym: ")
    data['words'].append(new_word)
    with open('dummy.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({'message': 'Word added successfully'}), 201

# Route to add antonyms for a specific word
@app.route('/words/<word>/antonym', methods=['POST'])
def add_antonym(word):
    data = read_json_file()
    antonym = input("Enter the antonym: ")
    for word_data in data['words']:
        if word_data['word'] == word:
            word_data['antonym'] = antonym
            with open('dummy.json', 'w') as f:
                json.dump(data, f, indent=4)
            return jsonify({'message': 'Antonym added successfully'}), 201
    return jsonify({'error': 'Word not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
