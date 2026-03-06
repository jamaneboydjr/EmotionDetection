from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask"
    ],
    author="Your Name",
    description="AI-based Emotion Detector using Watson NLP",
    python_requires=">=3.8",
)
