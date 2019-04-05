#!/usr/bin/env python
import requests, os, json

apiUrl = 'http://localhost:9001'

newService = {
  "name": "r1",
  "action": "stop",
};
content_type = "application/json"
headers = {'content-type': content_type}


r = requests.post(apiUrl+'/service/process', json=newService, headers=headers)

print("Posted to API and received Status Code {} and {} Bytes of Response".format(r.status_code,r.text))

