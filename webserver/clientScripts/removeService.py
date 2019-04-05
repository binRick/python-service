#!/usr/bin/env python
import requests, os, json

apiUrl = 'http://localhost:9001'
newScript = """#!/bin/sh
exec 2>&1
exec setuidgid vpntech sleep 60"""


newService = {
  "name": "r1",
};
content_type = "application/json"
headers = {'content-type': content_type}


r = requests.post(apiUrl+'/service/remove', json=newService, headers=headers)

print("Posted to API and received Status Code {} and {} Bytes of Response".format(r.status_code,r.text))

