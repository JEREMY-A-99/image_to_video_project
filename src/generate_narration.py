'''
generate voice narration
'''

from gtts import gTTS
import os

def generate_narration(text, output_audio):
    """
    Converts text to speech and saves it as an MP3 file.

    :param text: Text to convert to speech.
    :param output_audio: Path to save the generated narration file.
    """
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(output_audio)
        print(f"Narration saved at {output_audio}")
    except Exception as e:
        print(f"Error generating narration: {e}")
