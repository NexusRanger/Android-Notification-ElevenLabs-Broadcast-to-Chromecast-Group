# this is run from message1_trigger.py
# Creation Script for say_or_fetch function 
# trigger say_or_fetch to create voice file mp3 from message.txt

import time
from message3_say_or_fetch import say_or_fetch

voice = "Bella" # Put req name here (Bella is default anyway if not specified)
with open(r'c:\Data\Python\VoiceFiles\message.txt', 'r') as f:
    text = f.read().strip()

say_or_fetch(text, voice)

print ("process: message2 finished")

time.sleep(5)  # keep cmd window open to check progress   

# you can leave out the 'voice' argument and it will use default voice set in say_or_fetch.py
# e.g.  say_or_fetch("Have a nice day")

# Voice Name Choice: (You don't need the codes but here they are anyway)
# "Bella" : "EXAVITQu4vr4xnSDxMaL",
# "Rachel": "21m00Tcm4TlvDq8ikWAM",
# "Domi"  : "AZnzlk1XvdvUeBnXmlld",
# "Antoni": "ErXwobaYiN019PkySvjV",
# "Elli"  : "MF3mGyEYCl7XYWbV9V6O",
# "Josh"  : "TxGEqnHWrfWFTfGW9XjX",
# "Arnold": "VR6AewLTigWG4xSOukaG",
# "Adam"  : "pNInz6obpgDQGcFmaJgB",
# "Sam"   : "yoZ06aMxZJJ28mfd3POQ",
# "Test"  : "3KehPe3gxEYqOFSGDzGM"     # Not sure what Test does?

#input("Press Enter to continue...")

