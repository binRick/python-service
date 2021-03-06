#!/usr/bin/env python
import requests, os, json

apiUrl = 'http://localhost:9001'
newScript = """#!/bin/sh
exec 2>&1
exec setuidgid rick echo ok"""


newService = {
  "name": "r1",
  "script": newScript,
};
content_type = "application/json"
headers = {'content-type': content_type}


r = requests.post(apiUrl+'/service/create', json=newService, headers=headers)

print("Posted to API and received Status Code {} and {} Bytes of Response".format(r.status_code,r.text))

