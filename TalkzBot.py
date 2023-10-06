"""
# 日食・月振が、二色・ゲッシンみたいになる
import whisper
model = whisper.load_model("base")
result = model.transcribe("nisshoku.m4a")
print(result["text"])
"""

import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import openai
from janome.tokenizer import Tokenizer

#openai.api_key = "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"
#OPENAI_CHARACTER_PROFILE = "これから会話を行います。"

def stt(audio):
    try:
        # r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        output = r.recognize_google(audio, language="ja-JP", show_all=False)
        #print("Google Speech Recognition thinks you said\n" + r.recognize_google(audio, language="ja-JP", show_all=True))
        return output
    except sr.UnknownValueError:
        return "マイクが認識できません"
    except sr.RequestError as e:
        return f"リクエストエラー : {e}"

def gen_mp3(text):
    tts = gTTS(text=text, lang="ja")
    tts.save("output.mp3")
    print("音声ファイルを保存しました")

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

text = stt(audio)
print(text)

gen_mp3(text)

"""
# ChatGPT からトークデータを取得
response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo'
    , temperature = 0.5
    , messages = [
        {
            'role': 'system'
            , 'content': OPENAI_CHARACTER_PROFILE.strip()
        }
        , {
            'role': 'user'
            , 'content': text
        }
    ]
)
"""
"""
response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=text,
                temperature=0.0,
)
"""

def get_gpt_response(input_text):
    # ChatGPTに対話を送信して応答を取得
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=50,  # 応答の最大トークン数を設定
        temperature=0.7  # 応答のランダム性を制御
    )
    
    # ChatGPTからの応答を返す
    return response.choices[0].text
print(get_gpt_response(text))
#ai_message = response['choices'][0]['message']['content']
#print(ai_message)


"""
t = Tokenizer()
for token in t.tokenize(text):
    features = token.part_of_speech.split(",")
    if features[0] == "名詞":
        print(token.surface)
    print(token)
"""