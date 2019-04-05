#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR
pip install ansible --user
pip install flask --user
pip install lxml --user
pip install bson --user
pip install tai64n --user
cd installer && ansible-playbook -i localhost, playbooks/daemontools.yaml

