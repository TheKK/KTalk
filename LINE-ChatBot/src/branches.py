# -*- coding: utf-8 -*-

from pprint import pprint
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

    def show_branch_direction(self):
        allBranches = self.branches.json()['branches']
        latitude = 24.786576
        longitude = 120.996787
        addr = '300, Taiwan, Hsinchu City, East District \xe5\x85\x89\xe6\x98\x8e\xe9\x87\x8c'
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=%f,%f&destinations=' % (latitude, longitude)

        best_dest_index = 0
        best_dest_value = 10000000000000
        best_dest_time = ''
        best_dest_addr = ''

        for branch in self.branches.json()['branches']:
                result = requests.get(url + branch['dept_address'])
                dists = result.json()
                if len(dists['rows']) == 0:
                        continue

                elements = dists['rows'][0]['elements']
                dest_addrs = dists['destination_addresses']
                for index in range(0, len(elements)):
                        element = elements[index]
                        if element['status'].lower() != 'ok':
                                continue

                        value = element['duration']['value']
                        time = element['duration']['text']
                        if value <= best_dest_value:
                                best_dest_value = value
                                best_dest_index = index
                                best_dest_time = time
                                best_dest_addr = dest_addrs

        print(best_dest_addr)
        print(best_dest_time)

        return {"address": best_dest_addr, "time": best_dest_time}
