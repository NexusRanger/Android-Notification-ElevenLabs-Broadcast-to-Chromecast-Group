# This is script to copy into Eventghost - Add Action - Python Script

# catch autoremote message and write it to a pc file
# note you can't test this with Test button, it has to have input from autoremote
import os
import logging
import datetime

# Configure logging, define log file path
log_file = r"C:\Data\Python\VoiceFiles\log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG)

# Get the message from the payload & stringify
message = eg.event.payload
message = str(message)

# Remove the first 11, and last 1 characters from the message
message = message[11:]
message = message[:-1]

# Remove any unwanted characters 
message = message.replace(",", ",,")      # add extra pause
message = message.replace(" - Home", "")
message = message.replace("|", "")
message = message.replace("(", "")
message = message.replace(")", "")
message = message.replace("-", "")
message = message.replace("!", "")

#message = "hello its tuesday"    # testing

# create a log file
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
timestamp = datetime.datetime.now().strftime("%H:%M:%S")
logging.debug(timestamp +": "+message)

#file_path = r'C:\Data\Python\VoiceFiles\message.txt'  # for testing
#with open(file_path, 'w') as f:
#    f.write('Hello, world!')

# Define the path to the message file
file_path = r"C:\Data\Python\VoiceFiles\message.txt"

# Write the message value to the file
with open(file_path, "w") as f:
    f.write(str(message))
 
