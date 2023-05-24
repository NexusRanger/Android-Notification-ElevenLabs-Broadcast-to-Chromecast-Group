# purpose: to start process: message2
import subprocess

python_path = r"C:\Program Files\Python311\python.exe"
script_path = r"c:\data\python\VoiceFiles\message2_say_or_fetch_run.py"

# Run the script using the subprocess module
subprocess.run([python_path, script_path])
print ("process: message1 finished")

#input("Press Enter to continue...")    # use if pause req
