import requests
from requests.auth import HTTPBasicAuth

class FetchRPC():
    def __init__(self, url, auth=None):
        """
        url: http://my.ip.goes.here:9999/whatever
        auth: ("user", "pass")
        """
        self.url = url
        self.auth = auth
        self.session_id = ""
        self.headers = {
            "X-Transmission-Session-Id": self.session_id
        }
    def post(self, json_data="{}"):
        """
        Return of the request object we send to the RPC
        """
        if not self.auth:
            return requests.post( self.url, json=json_data, headers=self.headers )
        
        return requests.post( self.url, json=json_data, headers=self.headers, 
                    auth=HTTPBasicAuth( self.auth[0], self.auth[1] ) )

    def get_session_id(self):
        """
        Gets the X-Transmission-Session-Id header value due to CORS
        """
        r = self.post("{'test': 'test'}")
        session_id = r.text.split("X-Transmission-Session-Id:")[-1].replace("</code></p>", "").strip()
        self.session_id = session_id
        self.headers["X-Transmission-Session-Id"] = session_id
