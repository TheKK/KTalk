# -*- coding: utf-8 -*-

import requests

url = 'https://eospu.esunbank.com.tw/esun/bank/hackathon/atms?client_id=01940f38-4b11-4d55-b6ae-41af2145b699'
auth = {
    'Authorization': 'fP7XfLatwhrtu0sATfnZNR7LGPaLXiZ7BKzLdZI'
}

class Atm:
    def __init__(self):
        self.atms = requests.get(url, headers=auth)
        pass

    def get_all_atms(self):
        return self.atms.json()

