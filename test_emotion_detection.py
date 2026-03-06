"""
Unit tests for the emotion detection function.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Test cases for emotion_detector.
    """

    def test_joy(self):
        """
        Test dominant emotion as joy.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """
        Test dominant emotion as anger.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """
        Test dominant emotion as disgust.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """
        Test dominant emotion as sadness.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """
        Test dominant emotion as fear.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_invalid_text(self):
        """
        Test invalid empty input.
        """
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
