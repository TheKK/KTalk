# -*- coding: utf-8 -*-

import requests

url = 'https://eospu.esunbank.com.tw/esun/bank/hackathon/news?client_id=01940f38-4b11-4d55-b6ae-41af2145b699'
auth = {
    'Authorization': 'fP7XfLatwhrtu0sATfnZNR7LGPaLXiZ7BKzLdZI'
}
news = requests.get(url, headers=auth)

def get_all_news():
    return news.json()

def get_lastest_news():
    all_news = get_all_news()

    def extract_time(json):
        try:
            return int(json['pub_date'].encode('hex'), 16)
        except ValueError:
            return 0

    return sorted(all_news['news'], key=extract_time, reverse=True)[0]
