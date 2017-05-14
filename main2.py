import face_api, sms
import base64

fname = raw_input("File name: ")
name = raw_input("Name: ")

f = open(fname)
img = base64.b64encode(f.read())
f.close()

print face_api.enroll_face(img, name)
