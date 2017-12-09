import requests
import base64
import hmac
import hashlib
from hashlib import sha384
import json

base_url = 'https://api.gemini.com/v1/'

url = base_url + raw_input('Enter URL extension for https://api.gemini.com/v1/')

gemini_api_key = "jJSqhadscIz4PrVvYHDw" #api main key
gemini_api_secret_partial = "87Qx5EQMcGDAxVZAjEiHkwaX"  #last 3 is ezu

gemini_api_secret = gemini_api_secret_partial + raw_input("Enter API Secret Key PIN: ")

#api SECRET for security purposes, have user input last couple characters of key
