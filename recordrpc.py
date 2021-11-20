import logging, parserpc

class recordRPC():
    """
    Class for recording the RPC to handle any complex logic.
    Requires a full raw dictionary response, including tag, as well an a dao
    """


    def __init__(self, raw_response, dao) -> None:
        self.raw_response = raw_response
        self.dao = dao
        self.parser = parserpc.parseRPC()
        self.dt = self.parser.get_current_datetime()


    def record_peers(self) -> None:
        """
        Record peers from raw_response to the local DB into table peers
        """

        tag_value = self.raw_response['tag'] # Get tag

        for torrent in self.raw_response["arguments"]["torrents"]:
            t_name = torrent['name'] # Get torrent name

            peers = self.parser.peers(torrent["peers"])

            for d in peers: # Add tag, datetime, torren_name to the values to be inserted
                d["keys"] += f",tag,date,torrent_name"
                d["values"] += f",{tag_value},{self.dt},{t_name}"

                self.dao.insert("peers", d["values"])