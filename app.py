from flask import Flask, render_template, request
import datetime
import os
from services.emotion_service import detect_emotion_and_intensity
from services.speech_service import generate_speech

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text'].strip()
        if text:
            # Controller calls services
            emotion, confidence, rate, pitch, volume = detect_emotion_and_intensity(text)
            
            os.makedirs('static', exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            filename = f"static/empathy_{emotion.lower()}_{timestamp}.mp3"
            
            # Generate speech
            generate_speech(text, rate, pitch, volume, filename)
            
            return render_template('index.html', 
                                   filename=filename, 
                                   emotion=emotion, 
                                   confidence=confidence)
    
    return render_template('index.html')

if __name__ == '__main__':
    print("🚀 Empathy Engine running at http://127.0.0.1:5000")
    print("   → MVC Structure + Modern UI + Full Pitch Control")
    app.run(debug=True)