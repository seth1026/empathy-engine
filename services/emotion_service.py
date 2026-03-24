from transformers import pipeline

# Load model once when service is imported
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

def detect_emotion_and_intensity(text: str):
    text_lower = text.lower().strip()

    # Special handling for questions
    if text.endswith('?') or any(word in text_lower for word in ['how', 'what', 'why', 'when', 'can you', 'tell me']):
        emotion = "Inquisitive"
        base_rate = "+0%"
        base_pitch = "+0Hz"
        base_volume = "+0%"
        confidence = 0.95
    else:
        result = emotion_pipeline(text)[0]
        label = result['label']
        confidence = result['score']

        mapping = {
            "joy": "Happy", "sadness": "Sad", "anger": "Frustrated",
            "fear": "Concerned", "surprise": "Surprised",
            "disgust": "Frustrated", "neutral": "Neutral"
        }
        emotion = mapping.get(label, "Neutral")

        params = {
            "Happy":      ("+25%", "+8Hz", "+5%"),
            "Sad":        ("-20%", "-10Hz", "-8%"),
            "Frustrated": ("-10%", "-5Hz", "-3%"),
            "Concerned":  ("-12%", "-8Hz", "-5%"),
            "Surprised":  ("+30%", "+15Hz", "+10%"),
            "Inquisitive":("+0%", "+5Hz", "+0%"),
            "Neutral":    ("+0%", "+0Hz", "+0%")
        }
        base_rate, base_pitch, base_volume = params.get(emotion, ("+0%", "+0Hz", "+0%"))

    # Intensity scaling
    intensity = confidence
    rate_mult = 1 + intensity * 0.6
    pitch_mult = 1 + intensity * 0.8
    volume_mult = 1 + intensity * 0.5

    base_rate_num = int(base_rate.replace('%', ''))
    base_pitch_num = int(base_pitch.replace('Hz', ''))
    base_volume_num = int(base_volume.replace('%', ''))

    rate = f"{int(base_rate_num * rate_mult):+d}%"
    pitch = f"{int(base_pitch_num * pitch_mult):+d}Hz"
    volume = f"{int(base_volume_num * volume_mult):+d}%"

    return emotion, round(confidence, 2), rate, pitch, volume