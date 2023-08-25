#!/usr/bin/env bash
cd `dirname $0`
set -euxo pipefail 
# python -m venv env
# source env/bin/activate
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install -r requirements.txt

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec python3 -m src.main $@
# deactivate
