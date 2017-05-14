import base64, subprocess
from cv2 import *

def capture():
    #returns picture in base64 encoding

    #save image from webcam as temp.jpg
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()

    if s:
        imwrite("temp.jpg", img)

        #convert image file to b64
        f = open("temp.jpg","rb")
        b64img = base64.b64encode(f.read())
        f.close()

        #delete temp.jpg
        subprocess.call("rm temp.jpg")

        return b64img
    else:
        print "Error taking picture!"
        return
