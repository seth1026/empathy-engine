# 🎙️ The Empathy Engine - Giving AI a Human Voice

**A sophisticated AI service that detects emotions from text and delivers emotionally expressive speech using high-quality neural voices.**

## ✨ Features

### Core Requirements 
- **Text Input**: Clean web interface
- **Emotion Detection**: Sophisticated pre-trained model
- **Vocal Parameter Modulation**: Rate + Pitch + Volume (3 parameters)
- **Emotion-to-Voice Mapping**: Clear intensity-aware logic
- **Audio Output**: High-quality `.mp3` files with instant playback

### Wow Factors & Stretch Goals 
- **Granular Emotions**: 7 distinct emotions (Happy, Sad, Frustrated, Concerned, Surprised, Inquisitive, Neutral)
- **Intensity Scaling**: Dynamic scaling based on model confidence
- **Modern Web Interface**: Premium, responsive UI with glassmorphism design
- **Advanced Prosody Control**: Full SSML-style pitch, rate & volume modulation
- **Clean Architecture**: MVC (Model-View-Controller) pattern

## 🎯 Emotion-to-Voice Mapping

Uses **Hugging Face’s `j-hartmann/emotion-english-distilroberta-base`** (exactly as recommended in the challenge document).

## 🛠️ Tech Stack & Architecture

- **Framework**: Flask
- **Emotion Detection**: Hugging Face `transformers`
- **Text-to-Speech**: `edge-tts` (Microsoft neural voices with full prosody support)
- **Architecture**: **MVC (Model-View-Controller)** for clean, maintainable, and professional code organization

## 📂 Project Structure
├── 📁 services
│   ├── 🐍 emotion_service.py
│   └── 🐍 speech_service.py
├── 📁 static
│   ├── 🎵 empathy_concerned_105657.wav
│   ├── 🎵 empathy_concerned_105700.wav│
├── 📁 templates
│   └── 🌐 index.html
├── 📝 Readme.md
├── 🐍 app.py
└── 📄 requirements.txt

## 🚀 Installation & Setup

1. Clone the repository:
   git clone <https://github.com/seth1026/empathy-engine.git>
   cd empathy-engine

2. Create and activate virtual environment:
   python -m venv .venv
   .venv\Scripts\activate      # On Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Open http://127.0.0.1:5000 in your browser.

## 📝 Notes on Design Choices & Emotion-to-Voice Mapping Logic

### Architecture Decision
I adopted the **MVC (Model-View-Controller)** pattern to keep the code clean, modular, and maintainable:
- **Model**: `services/emotion_service.py` & `services/speech_service.py`
- **View**: `templates/index.html`
- **Controller**: `app.py`

### Emotion Detection
- Used **Hugging Face transformers** with the pre-trained model `j-hartmann/emotion-english-distilroberta-base` (exactly as recommended in the challenge document).
- This provides 7 granular emotions with confidence scores: joy, sadness, anger, fear, surprise, disgust, neutral.
- Added custom rule-based logic to detect **Inquisitive** for question sentences.

### Emotion-to-Voice Mapping Logic (Core Design Decision)

The service maps detected emotions to vocal parameters using the following logic:

| Emotion      | Base Rate | Base Pitch | Base Volume | Reasoning                          |
|--------------|-----------|------------|-------------|------------------------------------|
| Happy        | +25%      | +8Hz       | +5%         | Energetic, uplifting tone          |
| Sad          | -20%      | -10Hz      | -8%         | Slower, lower, softer voice        |
| Frustrated   | -10%      | -5Hz       | -3%         | Slightly tense and urgent          |
| Concerned    | -12%      | -8Hz       | -5%         | Careful and worried tone           |
| Surprised    | +30%      | +15Hz      | +10%        | Excited and raised pitch           |
| Inquisitive  | +0%       | +5Hz       | +0%         | Natural questioning tone           |
| Neutral      | +0%       | +0Hz       | +0%         | Default conversational voice       |

**Intensity Scaling**: The model’s confidence score (0.0–1.0) acts as a multiplier to make stronger emotions produce more dramatic changes in rate, pitch, and volume.

**TTS Engine**: Switched to `edge-tts` (Microsoft neural voices) instead of `pyttsx3` because it supports true prosody control (rate, pitch, volume) — enabling much more natural and emotionally expressive speech.

### Why These Choices?
- **Accuracy & Sophistication**: Hugging Face model is far superior to basic sentiment libraries like VADER/TextBlob.
- **Natural Sound**: Microsoft neural voices sound significantly more human-like.
- **Full Vocal Control**: True pitch adjustment (stretch goal fully achieved).
- **User Experience**: Modern glassmorphism UI with instant audio playback and one-click examples.
- **Code Quality**: MVC architecture demonstrates strong software engineering practices and makes the code easy to maintain and extend.