# SmartDoor
A doorbell that can tell you who's at the door!

Made at Atomhacks.

## _Notice_

This program got majorly messed up at the hackathon, including the website being taken down,
which is easily 1/2 of the functionality.
However, the basic API still works. This was designed to be run on a raspberry pi, but can run
anywhere if you only use `test-main.py`.
I may get back and fix this project eventually.

## _Setup_

To use, you must obtain a Kairos facial recognition and Nexmo API key. Plug these in to 
the files `sms.py` and `face_api.py`.
Next, enter in your nexmo number and the number you would like messages to be sent to in `face_api.py`.
Also, make sure that your webcam is in `/dev/video0`. If not, then change it in picture.py.
Finally, install `OpenCV`. This varies from system to system, so you're on your own.
This step is optional if you only want to use the recognition and sms portions of the program.

## _Usage_

Run `enroll.py` with a picture and name to register the face to that name.
Run `main.py` if you have `OpenCV` installed and a webcam plugged it. It will take a picture using the webcam.
Alternatively, take any picture you'd like, and then run `test-main.py`, and enter the path to the picture.
Both of these will identify the face or notify you if it hasn't been added.
There was an aforementioned website functionality, which is not currently working, even though it is
still in the code.
