import requests

url = 'https://eospu.esunbank.com.tw/esun/bank/hackathon/finance_news?client_id=01940f38-4b11-4d55-b6ae-41af2145b699'
auth = {
    'Authorization': 'fP7XfLatwhrtu0sATfnZNR7LGPaLXiZ7BKzLdZI'
}
finance_news = requests.get(url, headers=auth)

def get_all_finance_news():
    return finance_news.json()

def get_lastest_finance_news():
    all_finance_news = get_all_finance_news()

    def extract_time(json):
        try:
            return int(json['pub_date'].encode('hex'), 16)
        except ValueError:
            return 0

    return sorted(all_finance_news['finance_news'], key=extract_time, reverse=True)[0]
