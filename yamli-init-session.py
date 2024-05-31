import os
import pickle
import requests

def initialize_session():
    session = requests.Session()
    with open('/tmp/yamli_session.pkl', 'wb') as f:
        pickle.dump(session, f)

def main():
    initialize_session()
    print("Session initialized")

if __name__ == "__main__":
    main()

