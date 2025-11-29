from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Mongolian Sentence Checker Backend is running.'})

@app.route('/check_sentence', methods=['POST'])
def check_sentence():
    data = request.get_json()
    sentence = data.get('sentence')
    if not sentence:
        return jsonify({'success': False, 'message': 'No sentence provided.'}), 400
    return jsonify({'success': True, 'sentence': sentence, 'message': 'Sentence received successfully.'})

if __name__ == '__main__':
    app.run(debug=True)