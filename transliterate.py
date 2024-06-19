import sys
import requests
import json
import pickle

config = json.load(open('config.json', 'r'))
yamli_credentials = config["yamli-credentials"]

def load_session():
    with open('/tmp/yamli_session.pkl', 'rb') as f:
        session = pickle.load(f)
    return session

def query_yamli_api(query, session):
    url = "https://api.yamli.com/transliterate.ashx"
    params = {
        "word": query
    }
    params.update(yamli_credentials)

    response = session.get(url, params=params)
    if response.status_code == 200:
        return response.json()["r"].split('|')
    return []

def strip_suffixes(word):
    return word.split('/')[0]

def generate_alfred_items(results):
    items = []
    for result in results[:3]:
        stripped_result = strip_suffixes(result)
        items.append({
            "title": stripped_result,
            "arg": stripped_result
        })
    return items

def main():
    query = " ".join(sys.argv[1:])
    if query:
        session = load_session()
        results = query_yamli_api(query, session)
        items = generate_alfred_items(results)
        alfred_output = {"items": items}
        print(json.dumps(alfred_output))

if __name__ == "__main__":
    main()
