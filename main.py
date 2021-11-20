## Local imports
import fetchrpc

URL = "http://192.168.0.250:9091/transmission/rpc"
AUTH = ("admin", "Jsquad42069")

def main():
    frpc = fetchrpc.FetchRPC(URL, AUTH)
    frpc.get_session_id()

    print(frpc.post("{'test': 'test'}").content)


if __name__ == "__main__":
    main()