## Local imports
import fetchrpc, parserpc

# Standard library
import logging
logging.basicConfig(format='%(asctime)s |%(levelname)s| %(message)s', 
                    datefmt='%m/%d/%Y-%I:%M:%S_%p', 
                    level=logging.DEBUG)

URL = "http://192.168.0.250:9091/transmission/rpc"
AUTH = ("admin", "Jsquad42069")

def main() -> None:
    frpc = fetchrpc.FetchRPC(URL, AUTH)
    frpc.get_session_id()

    par = parserpc.parseRPC()
    mydict = par.js_to_dict(frpc.get_all_stats())

    print(par.peers(mydict["arguments"]["torrents"][0]["peers"]))


if __name__ == "__main__":
    main()