import urllib
import urllib2

key = 'a538ddad'
secret = '2c0f1a2d9323655d'
to = '16465892931'
sender = '12035298897'

def send_sms(text):
    params = {
    'api_key': key,
    'api_secret': secret,
    'to': to,
    'from': sender,
    'text': text + "\n"
    }

    url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

    request = urllib2.Request(url)
    request.add_header('Accept', 'application/json')
    response = urllib2.urlopen(request)
