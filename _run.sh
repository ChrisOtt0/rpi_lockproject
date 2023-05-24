#!/bin/bash

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $__dir

python button.py &
uvicorn server:app --host 0.0.0.0 --port 8080 --reload
