from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    try:
        audio_data = request.files['audio'].read()
        recognizer = sr.Recognizer()
        text = recognizer.recognize_google(audio_data)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()