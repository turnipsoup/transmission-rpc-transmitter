import json, logging

class parseRPC():
    def __init__(self) -> None:
        pass



    def js_to_dict(self, js):
        """
        Take a string of JSON and return a python dictionary
        """
        return json.loads(js)



    def dict_to_csv(self, pdict: dict) -> dict[str, str]:
        """
        Takes an object containing two CSVs:

        IN: {k1: v1, k2: v2}
        OUT: {'keys': 'k1,k2', 'values': 'v1,v2'}
        """

        csv = {
            "keys": ",".join([str(x) for x in pdict.keys()]),
            "values": ",".join([str(x) for x in pdict.values()])
        }

        return csv
        


    def peers(self, peers_json):
        """
        Take the peers response of a torrent and return an array of
        csv dictionaries [self.dict_to_csv] for each peer
        """

        peers_arr = []

        for peer in peers_json:
            peers_arr.append(self.dict_to_csv(peer))

        return peers_arr