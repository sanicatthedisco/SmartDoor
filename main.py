import face_api, sms, picture
import base64

img = picture.capture()
n = face_api.identify_face(img)
sms.send_sms(n)
