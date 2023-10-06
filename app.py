"""
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
    app.run(port=5500)
"""
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="名前を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    # GET送信の処理
    field = request.args.get("field","")
    return render_template('result.html', message = "名前は{}です。".format(field))

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form["field"]
    print(field)
    return render_template('result.html', message = "名前は{}です。".format(field))

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')