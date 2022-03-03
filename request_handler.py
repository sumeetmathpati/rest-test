import requests
import json

headers = {
    "Accept": "*/*",
    "User-Agent": "httpp://rest-tool.com" 
}

class RequestHandler():

    def __init__(self, url, method="GET", headers=headers, payload=""):

        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload = ""
    
    def send(self):
        
        response = requests.request(self.method, self.url, data=self.payload, headers=self.headers)
        # print(response.content)
        if "application/json" in response.headers["Content-Type"]:
            return ("json", json.dumps(response.json(), sort_keys=True, indent=4))

        if "text/html" in response.headers["Content-Type"]:
            return ("html", response.text)