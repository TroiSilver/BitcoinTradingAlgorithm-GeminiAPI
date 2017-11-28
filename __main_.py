import requests
import base64
import hmac
import hashlib
from hashlib import sha384
import json

url = "https://api.gemini.com/v1/order/status"

gemini_api_key = "mykey"
gemini_api_secret = "1234abcd"

# for the purposes of this example, we've shown hand-rolled JSON - please import json and use json.dumps in your real code!
b64 = base64.b64encode("""{
    "request": "/v1/order/status",
    "nonce": 123456,

    "order_id": 18834
}
""")

json_string = """{
    "request": "/v1/order/status",
    "nonce": 123456,
    "order_id": 18834
}
"""
print json_string
json_string2 = json.dumps({'request': '/v1/order/status', 'nonce': 123456, 'order_id': 18834}, indent=4, separators=(',', ': '))
print json_string2
print base64.b64encode(json_string2)
print base64.b64encode(json_string)
print b64

signature = hmac.new("1234abcd", b64, hashlib.sha384).hexdigest()

headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
