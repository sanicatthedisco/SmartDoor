import face_api, sms
import base64

fname = raw_input("File name: ")
#name = raw_input("Name: ")

f = open(fname)
img = base64.b64encode(f.read())
f.close()

n = face_api.identify_face(img)
sms.send_sms(n)
