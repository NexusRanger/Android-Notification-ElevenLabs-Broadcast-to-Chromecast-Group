# First time of voicing a phrase, this uses ElevenLabs to create a sound file mp3
# Errors 'should' default to pyttsx3
# Subesequent requests should look up the local mp3 file instead

# take phrase from 'messages.txt' to create sound file. Speak it (PC) or cast it or both
# speaking will be passed to message4_cast.py to cast the audio

import os
import string
import requests
import io
from pydub import AudioSegment
from playsound import playsound
import pyttsx3
import subprocess
import time

# Configuration
SPEED = 0.95     # you can change the pitch of the saved file if req
FOLDER_PATH = "C:\\Data\\Python\\VoiceFiles"  # add to environment variables: 'path'
DEFAULT = "Bella"
API_KEY = "*************************"  # Limited Free: https://beta.elevenlabs.io/

PLAY_AUDIO = True  # Set to True to play the audio on PC speakers
CAST_AUDIO = True  # Set to True to cast the audio to Chromecasts / group

voices = {
    "Bella":  "EXAVITQu4vr4xnSDxMaL",
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Domi"  : "AZnzlk1XvdvUeBnXmlld",
    "Antoni": "ErXwobaYiN019PkySvjV",
    "Elli"  : "MF3mGyEYCl7XYWbV9V6O",
    "Josh"  : "TxGEqnHWrfWFTfGW9XjX",
    "Arnold": "VR6AewLTigWG4xSOukaG",
    "Adam"  : "pNInz6obpgDQGcFmaJgB",
    "Sam"   : "yoZ06aMxZJJ28mfd3POQ",
    "Test"  : "3KehPe3gxEYqOFSGDzGM"     # Not sure what Test does?
}

def say_or_fetch(text, name=DEFAULT):
    """
    Say or fetch the audio for the given text using the specified voice.
    Args:
        text (str): The text to be spoken or fetched.
        name (str): The name of the voice to use.
    Raises:
        ValueError: If the provided voice name is invalid.
    """
    folder_path = FOLDER_PATH
    # Remove any invalid characters from the filename
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in text if c in valid_chars)
    filename = filename.replace(' ', '_') + '.mp3'

    # Get the voice code
    voice = voices.get(name)
    if not voice:
        raise ValueError("Invalid voice name")

    audio_file_path = os.path.join(folder_path, filename)

    if os.path.exists(audio_file_path):
        # File exists
        print(f"message3 local file: {audio_file_path}")
        if PLAY_AUDIO:
            play_audio(audio_file_path)
        if CAST_AUDIO:
            cast_audio()

    else:
        # File doesn't exist, generate and save it
        print(f"Generating new audio file using Eleven Labs API")
        try:
            audio_data = generate_audio(text, voice, SPEED, audio_file_path)
            save_audio(audio_data, audio_file_path)
            if PLAY_AUDIO:
                play_audio(audio_file_path)
            if CAST_AUDIO:
                cast_audio()
        except Exception as e:
            # Handle any errors gracefully
            print(f"Error: {e}")
            tts_speech(text)

def generate_audio(text, voice, speed=1.0, audio_file_path=None):
    """
    Generate audio data for the given text using the specified voice.
    Args:
        text (str): The text to generate audio for.
        voice (str): The voice code.
        speed (float): The speed factor for the audio.
        audio_file_path (str): The file path to save the audio to.
    Returns:
        bytes: The generated audio data.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY,
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0,
        },
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    audio_data = response.content

    # Change speed of audio data
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
    audio_segment = audio_segment._spawn(audio_segment.raw_data, overrides={"frame_rate": int(audio_segment.frame_rate * speed)})

    if audio_file_path:
        # Save audio data to file
        with open(audio_file_path, "wb") as f:
            audio_segment.export(f, format="mp3")

    return audio_segment.export(format="mp3").read()

def play_audio(audio_file_path):
    playsound(audio_file_path)

def save_audio(audio_data, audio_file_path):
    with open(audio_file_path, "wb") as f:
        f.write(audio_data)

def tts_speech(text):               # fallback on error
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()        

print ("process: message3 finished")

# run message4 to cast the mp3
def cast_audio():
    python_path = r"C:\Program Files\Python311\python.exe"
    script_path = r"C:\Data\Python\VoiceFiles\message4_cast.py"
    subprocess.run([python_path, script_path])

# TESTING: say "*****" on PC (and cast stored message.txt) if script is run as main()
# this is only exec if you run this script on it's own, for testing purposes
def main():
    try:
        say_or_fetch("hello world")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Process: (Main) message3 finished")

if __name__ == "__main__":   # if script is run stand-alone, not called
    main()

    #input("Press Enter to continue...")

