## Local imports
import fetchrpc, parserpc, dao

# Standard library
import logging
logging.basicConfig(format='%(asctime)s |%(levelname)s| %(message)s', 
                    datefmt='%m/%d/%Y-%I:%M:%S_%p', 
                    level=logging.DEBUG)


URL = "http://192.168.0.250:9091/transmission/rpc"
AUTH = ("admin", "Jsquad42069")

def main() -> None:
    logging.info("Starting up")
    
    frpc = fetchrpc.FetchRPC(URL, AUTH)
    frpc.get_session_id()

    par = parserpc.parseRPC()
    mydict = par.js_to_dict(frpc.get_all_stats())

    d_ao = dao.DAO("test.db")

    for peer in mydict["arguments"]["torrents"][0]["peers"]:
        d_ao.insert("peers", par.dict_to_csv(peer)["values"])


if __name__ == "__main__":
    main()