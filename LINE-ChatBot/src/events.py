import requests

url = 'https://eospu.esunbank.com.tw/esun/bank/hackathon/events?client_id=01940f38-4b11-4d55-b6ae-41af2145b699'
auth = {
    'Authorization': 'fP7XfLatwhrtu0sATfnZNR7LGPaLXiZ7BKzLdZI'
}
events = requests.get(url, headers=auth)

def get_all_events():
    return events.json()

def get_lastest_event():
    all_events = get_all_events()

    def extract_time(json):
        try:
            return int(json['pub_date'].encode('hex'), 16)
        except ValueError:
            return 0

    return sorted(all_events['events'], key=extract_time, reverse=True)[0]
