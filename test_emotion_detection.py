import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        # Test statement expecting dominant emotion: joy
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result.get('dominant_emotion'), 'joy', 
                         f"Expected 'joy' but got {result.get('dominant_emotion')}")

    def test_anger(self):
        # Test statement expecting dominant emotion: anger
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result.get('dominant_emotion'), 'anger', 
                         f"Expected 'anger' but got {result.get('dominant_emotion')}")

    def test_disgust(self):
        # Test statement expecting dominant emotion: disgust
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result.get('dominant_emotion'), 'disgust', 
                         f"Expected 'disgust' but got {result.get('dominant_emotion')}")

    def test_sadness(self):
        # Test statement expecting dominant emotion: sadness
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result.get('dominant_emotion'), 'sadness', 
                         f"Expected 'sadness' but got {result.get('dominant_emotion')}")

    def test_fear(self):
        # Test statement expecting dominant emotion: fear
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result.get('dominant_emotion'), 'fear', 
                         f"Expected 'fear' but got {result.get('dominant_emotion')}")

if __name__ == '__main__':
    unittest.main()
