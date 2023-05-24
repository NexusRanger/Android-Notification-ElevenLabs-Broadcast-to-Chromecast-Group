# Android-Notification-Broadcast-to-Chromecast-Group

Uses ElevenLabs voice generation

Tasker Autonotification > Eventghost > Python > Chromecasts

1. Add a Tasker Profile to catch any notification

2. Use Autoremote to forward that to Eventghost with message preamble "user==:==" followed by either 
   the Tasker variables, or your own message to voice announce...
   
   For example: "user==:== Attention, Spacex launch in one hour"

3. Set up Eventghost to Trigger on "AutoRemote.Message.user="

4. After that trigger add the python script in the listed files

5. After that add a 'Start Application' action with (and note the "" are necessary for command line options)
 
   executable: C:\Program Files\Python311\python.exe 
   
   and command line options: "C:\Data\Python\VoiceFiles\message1_trigger.py" 
   
6. Put the other four python files into c:\data\python\voicefiles  
   
7. See if it works


Troubleshooting:

Read the python files for other settings and to add your ElevenLabs API Key

You may need to add the voicefiles folder path to PYTHONPATH and to Path

Chrome seems to work better to send the Autoremote message, but deselect the eventghost one if that causes double messages

ffmpeg errors: Check permissions on the message.txt file, or run Eventghost as Administrator

message arrives as %antext: That's a Tasker variable and is only available when triggered by actual notification not by test running the Task

