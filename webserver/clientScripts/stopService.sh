#!/bin/bash
curl -sX POST -d '{"name":"r1","action","stop"}' -H "Content-type: application/json" http://localhost:9001/service/process \

# | jq
