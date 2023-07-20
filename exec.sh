#!/usr/bin/env bash
cd `dirname $0`
set -eux
# python -m venv env
# source env/bin/activate

pip3 install -r requirements.txt

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec python3 -m src.main $@
# deactivate
