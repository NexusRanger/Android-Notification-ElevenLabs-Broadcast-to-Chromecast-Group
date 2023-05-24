# run python 'simple server' for chromecast to broadcast local mp3 file
import http.server
import socketserver
import threading
import pychromecast
import os
import socket

PORT = 8000  # change to match port number, 8000 is default
DURATION = 12 # secs to run server, though it will continue while file is playing
SERVE_DIR = r"C:\Data\Python\voicefiles"  # local mp3 files folder
LOCALIP = socket.gethostbyname(socket.gethostname()) # auto finds IP address 
GROUP = "All Speakers"   # edit this to chromecast or group name
CONTENT_TYPE = "audio/mp3" # content type of file # always mp3
VOLUME = 0.5

# find file_name from message.txt and swap spaces for underscore
# also remove any commas that were initially added to create a pause in the mp3
with open(r'c:\data\python\voicefiles\message.txt', 'r') as f:
    file_name = f.read().strip().replace(' ', '_').replace(',', '')

FILENAME = file_name + ".mp3" # file to broadcast (file in SERVE_DIR)
print (".\nFile to run: " + FILENAME)

class LoggingHandler(http.server.SimpleHTTPRequestHandler):
    def log_error(self, format, *args):
        print(f"Server error: {format % args}")

os.chdir(SERVE_DIR)   # open server in correct folder to find voice files

Handler = LoggingHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

def start_server():
    print(f"Starting server on {LOCALIP} port {PORT}")
    print(f"Server will run for {DURATION} seconds")
    httpd.serve_forever()

def stop_server():
    print(".")
    httpd.shutdown()
    httpd.server_close()

server_thread = threading.Thread(target=start_server)
server_thread.start()

threading.Timer(DURATION, stop_server).start()

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[GROUP])

cast = chromecasts[0]
cast.wait() 

mc = cast.media_controller

print ("FILENAME: "+FILENAME)
mc.play_media(f"http://{LOCALIP}:{PORT}/{FILENAME}", content_type=CONTENT_TYPE)

mc.block_until_active()

cast.set_volume(VOLUME) 
print("Group: '"+GROUP+"'" + " Volume: " + str(round(cast.status.volume_level, 1)))

print ("process: message4 finished")