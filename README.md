# Emotion Detector

This project is an AI-based web application that detects emotions in user-provided text using the IBM Watson NLP Emotion model.

## Features
- Emotion detection using Watson NLP
- Returns scores for:
  - anger
  - disgust
  - fear
  - joy
  - sadness
- Identifies the dominant emotion
- Flask-based web app
- Unit tests included
- Static code analysis ready with pylint

## Project Tasks Completed
- Task 1: Clone the project repository
- Task 2: Create an emotion detection application using the Watson NLP library
- Task 3: Format the output of the application
- Task 4: Package the application
- Task 5: Run Unit tests on your application
- Task 6: Web deployment of the application using Flask
- Task 7: Incorporate error handling
- Task 8: Run static code analysis

## Installation

```bash
git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector
pip install -r requirements.txt
```

## Run the application

```bash
python server.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Run unit tests

```bash
python -m unittest test_emotion_detection.py
```

## Run pylint

```bash
pylint EmotionDetection/emotion_detection.py
pylint server.py
```

## Example Input
```text
I am so happy today!
```

## Example Output
```text
For the given statement, the system response is 'anger': 0.01, 'disgust': 0.02, 'fear': 0.03, 'joy': 0.88 and 'sadness': 0.06. The dominant emotion is joy.
```
