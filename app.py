from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

app = Flask(__name__)

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            text = text.lower()
            rendered_template = render_template('index.html', text=text)
            play_Happy(text)
            return rendered_template
        except sr.UnknownValueError:
            text = "Sorry, I could not understand what you said."
            return render_template('index.html', text=text)
        
           
def play_Happy(instruction):
    if 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current timeis ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's Date: " + date)

    elif 'how are you' in instruction:
        talk("I' am Fine, how about you")

    elif 'kasa aahes' in instruction:
        talk("Areeee miii Bara aahe . Tu kasa aaahheesss?")

    elif 'name' in instruction:
        talk("'Hello there! My name is Happy Singh, and I'm here to assist you. How may I be of service to you today?'")

    elif 'nav' in instruction:
        talk("aaaa Namskarrr!!!, Maajh naav Happy Singh aahe, Miii ithhe tummhaaala madat karaaylaaa aaalloo aaheee")

    elif 'who' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')

if __name__ == '__main__':
    app.run(debug=True)
