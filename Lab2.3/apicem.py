#
#  Lab 2.3
#

import requests, json, pprint
url = 'https://sandboxapic.cisco.com/api/v1'
url1 = '/host'
url2 = '/network-device'
url3 = '/topology/physical-topology'
header = {"content-type": "application/json", "X-Auth-Token": "ST-467-mSNy6KuiAKtN2qUnZfHF-cas"}

resp_h = requests.get(url + url1, headers=header, verify=False)
resp_d = requests.get(url + url2, headers=header, verify=False)
resp_t = requests.get(url + url3, headers=header, verify=False)

print("Hosts = ")
pprint.pprint(json.dumps(resp_h.json()))
print("Devices = ")
pprint.pprint(json.dumps(resp_d.json()))
print("Topology = ")
pprint.pprint(json.dumps(resp_t.json()))

