import urllib
import urllib2

key = '{api id goes here}'
secret = '{secret goes here}'
to = '{recieving number goes here}'
sender = '{sending number goes here}'

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
