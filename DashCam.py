import tkinter as tk

from picamera import PiCamera
from time import sleep
from datetime import datetime

now = str(datetime.now())

camera = PiCamera()
camera.rotation = 90
#camera.start_preview(fullscreen=False, window = (100,20,640,480))
#sleep(5)
#camera.start_recording('/home/pi/DashCam/Video.h264')
#sleep(5)
#camera.stop_recording
#camera.stop_preview()

top = tk.Tk()

cameraOn = False

def helloCallBack():
   global cameraOn
   if cameraOn:
        camera.stop_recording()
        cameraOn = False
        camera.stop_preview()
   else:
        camera.start_preview()
        camera.start_recording("/home/pi/DashCam/"+now+".h264")
        cameraOn = True

B = tk.Button(top, text ="Record", command = helloCallBack)

B.pack()
top.mainloop()
