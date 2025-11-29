from flask import Flask, jsonify, request
from flask_cors import CORS
from grammar_checker import is_sentence_correct

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
    is_correct = is_sentence_correct(sentence)
    if is_correct:
        return jsonify({'success': True, 'sentence': sentence, 'message': 'Зөв өгүүлбэр!'}), 200
    else:
        return jsonify({'success': False, 'sentence': sentence, 'message': 'Буруу өгүүлбэр эсвэл үгсийн сан, дүрэмд байхгүй үг байна.'}), 200

if __name__ == '__main__':
    app.run(debug=True)