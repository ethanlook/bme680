#!/usr/bin/env bash

# bash safe mode. look at `set --help` to see what these are doing
set -euxo pipefail 

./setup.sh
source .env

cd $MODULE_DIR
ENTRYPOINT=src.main

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec $PYTHON -m $ENTRYPOINT $@
