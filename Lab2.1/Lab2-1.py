#
# Lab 2-1
#
import json
import requests
import pprint

URL = 'https://lookup.binlist.net/'
c_num = []
# bks = []
with open('C:\\Users\\resu\\p4ne\\Lab2.1\\card1.json') as data_file:
    data = json.load(data_file)
    c_num += [str(x['CreditCard']['CardNumber'])[0:8] for x in data]

for c in c_num:
    r = requests.get(URL + c, headers={'Accept-Version': "3"})
    if 200 <= r.status_code <= 299:
        #print(r.json())
        bks = r.json()
        #if (bks['bank']['name']) == True:
        print(bks['bank']['name'])




