import requests
import base64
import hmac
import hashlib
from hashlib import sha384
import json
import random


#todo Use hmac for ptp encryption :)
def generate_nonce(length):  #todo: change this to include file
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

base_url = 'https://api.sandbox.gemini.com/v1/'

sig = {}
headers = {}

url_extension = raw_input('Enter URL extension for ' + base_url)

url = base_url + url_extension

gemini_api_key = "jJSqhadscIz4PrVvYHDw" #api main key
gemini_api_secret_partial = "87Qx5EQMcGDAxVZAjEiHkwaX"  #last 3 is ezu



gemini_api_secret = gemini_api_secret_partial + raw_input("Enter API Secret Key PIN: ")

order_id = raw_input("Enter Order ID: ")


sig['request'] = "/v1/" + url_extension
sig['nonce'] = generate_nonce(25)
sig['symbol'] = "btcusd"


#api SECRET for security purposes, have user input last couple characters of key
print sig['nonce']

jsonSig = json.dumps(sig)

b64 = base64.b64encode(jsonSig)

print jsonSig
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

print(signature)


# headers = {}

# headers['Content-Type'] = "text/plain"
# headers['Content-Length'] = "0"
# headers['X-GEMINI-API-KEY'] = gemini_api_key
# headers['X-GEMINI-PAYLOAD'] = b64
# headers['X-GEMINI-SIGNATURE'] = signature
# headers['Cache-Control'] = "no-cache"
#
# headers = json.dumps(headers)

headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }
print headers

response = requests.request("POST", url, headers=headers)

print(response.text)