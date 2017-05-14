import base64, ast, datetime, json
from urllib import quote_plus, urlencode
from urllib2 import Request, urlopen

app_id = "3b54027c"
app_key = "a22a5d35b485afcc2157ae7b2ef6cbdc"

headers = {
  'Content-Type': 'application/json',
  'app_id': app_id,
  'app_key': app_key
}

def enroll_face(img, name):
    #img is base64
    #name is the name the subject should be entered with
    values = '{"image": "'+img+'","subject_id":"'+name+'","gallery_name":"MyGallery"}'
    
    request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

    response_body = urlopen(request).read()
    return response_body

def identify_face(img):
    #img is base64

    values = '{"image": "'+img+'","gallery_name":"MyGallery"}'

    request = Request('https://api.kairos.com/recognize', data=values, headers=headers)
    
    response_body = ast.literal_eval(urlopen(request).read())
    print response_body["images"][0]["transaction"]["subject_id"]
    
    try:
        response_body["images"]
        r = response_body["images"][0]["transaction"]
        if r["status"] == "failure":
            print "I don't know who's at the door! Go to the website later to tell me."
            params = {
                "time":get_time(),
                "gender":get_gender(img),
                "image":img,
            }
            req = Request("https://100.104.40.50/SmartDoor Portal/submit.php?time=10&gender=male&image=rwfojioewe")
            res = urlopen(req).read()
            print res
            return "I don't know who's at the door! Go to the website later to tell me."
        else:
            return r["subject_id"] + " is at the door!"
    except KeyError:
        #print "no faces found in image"
        return "There is no one at the door!"


def get_gender(img):
    #only supposed to operate when we know there's a face in the picture
    values = '{"image": "'+img+'"}'
    
    request = Request('https://api.kairos.com/detect', data=values, headers=headers)

    response_body = urlopen(request).read()

    g = ast.literal_eval(response_body)["images"][0]["faces"][0]["attributes"]["gender"]["type"]

    if g == "F":
        return "Female"
    else:
        return "Male"

def get_time():
    now = datetime.datetime.now()
    return str(now.hour) + ":" + str(now.minute)
