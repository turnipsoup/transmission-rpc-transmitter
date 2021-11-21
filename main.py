## Local imports
import fetchrpc, parserpc, recordrpc, dao

# Standard library
import logging
logging.basicConfig(format='%(asctime)s |%(levelname)s| %(message)s', 
                    datefmt='%m/%d/%Y-%I:%M:%S_%p', 
                    level=logging.DEBUG)


URL = "http://192.168.0.250:9091/transmission/rpc"
AUTH = ("admin", "<fancy-password-goes-here>")

def main() -> None:
    logging.info("Starting up")
    
    frpc = fetchrpc.FetchRPC(URL, AUTH)
    frpc.get_session_id()


    par = parserpc.parseRPC()
    rpcstats = par.js_to_dict(frpc.get_all_stats())

    



    d_ao = dao.DAO("test.db")

    rec = recordrpc.recordRPC(rpcstats, d_ao)
    rec.record_tor_stats()
    rec.record_peers()


if __name__ == "__main__":
    main()
