# -*- coding: utf-8 -*-

import requests

url = 'https://eospu.esunbank.com.tw/esun/bank/hackathon/branches?client_id=01940f38-4b11-4d55-b6ae-41af2145b699'
auth = {
    'Authorization': 'fP7XfLatwhrtu0sATfnZNR7LGPaLXiZ7BKzLdZI'
}

class Branch:
    def __init__(self):
        self.branches = requests.get(url, headers=auth)
        pass

    def get_all_branches(self):
        return self.branches.json()

