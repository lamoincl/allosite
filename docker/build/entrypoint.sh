#!/bin/sh

apk update
apk upgrade

/usr/local/bin/python -m pip install --upgrade pip
pip install -r requirements.txt

exec "$@"
