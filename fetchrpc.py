import requests, logging, uuid, random
from requests.auth import HTTPBasicAuth


class FetchRPC():
    def __init__(self, url: str, auth=None) -> None:
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


    def get_uuid(self):
        return uuid.uuid4()


    def post(self, json_data: dict) -> str:
        """
        POST JSON query to RPC, takes a dictionary
        Return a string of the JSON response
        """

        logging.debug(f"Sending request {json_data}")

        if not self.auth:
            return requests.post( self.url, json=json_data, headers=self.headers )
        
        return requests.post( self.url, json=json_data, headers=self.headers, 
                    auth=HTTPBasicAuth( self.auth[0], self.auth[1] ) ).text.strip()



    def get_session_id(self) -> None:
        """
        Gets the X-Transmission-Session-Id header value due to CORS
        """
        logging.info("Getting Session ID")

        try:
            r = self.post("{'test': 'test'}")
            session_id = r.split("X-Transmission-Session-Id:")[-1].replace("</code></p>", "").strip()
            logging.info(f"Returned Session ID: {session_id}")
            self.session_id = session_id
            self.headers["X-Transmission-Session-Id"] = session_id
        except:
            logging.error("Unable to get Session ID from response")
            self.session_id = ""
            self.headers["X-Transmission-Session-Id"] = session_id

    def get_all_stats(self) -> str:
        """
        Will get the following stats for all torrents:
            "name", 
            "status", 
            "uploadRatio", 
            "rateDownload", 
            "rateUpload", 
            "totalSize", 
            "peers"
        """

        logging.debug("Fetching all stats")

        post_json = {
            "arguments": {
                "fields": ["name", "status", "uploadRatio", "rateDownload", 
                                "rateUpload", "totalSize", "peers"]
            },
            "method": "torrent-get",
            "tag": int(str(int(self.get_uuid().hex, base=16))[:16]) # It returns the tag, so make the UUID an integer
        }

        resp = self.post(post_json).strip()
        logging.debug(f"Response: {resp}")
        return resp
