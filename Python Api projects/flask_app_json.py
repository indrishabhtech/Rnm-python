import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
@app.route('/age')
def get_users():
    # Read data from the JSON file
    with open('dummy.json') as f:
        data = json.load(f)
    users = data['users']
    return jsonify(users)

@app.route('/words')
def get_words():
    # Read data from the JSON file
    with open('dummy.json') as f:
        data = json.load(f)
    words = data['words']  # Access 'words' key first
    # return jsonify(words)
    
    
    # Create a list to store word and synonym pairs
    # word_synonym_list = []
    # for word_data in words:
    #     word_synonym_list.append({
    #         'word': word_data['word'],
    #         'synonym': word_data['synonym']
    #     })
    # return jsonify(word_synonym_list)


    # Create a list to store word and antonym pairs
    word_antonym_list = []
    for word_data in words:
        word_antonym_list.append({
            'word': word_data['word'],
            'antonym': word_data['antonym']
        })
        
        
    word = input("Enter the words to the Antonym ")
    print(word_data['antonym'])
    
    return jsonify(word_antonym_list)




if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)

