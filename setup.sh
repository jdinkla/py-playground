#!/bin/sh

ENV=pythonenv3.8
python3.8 -m venv ${ENV}
source ${ENV}/bin/activate

pip install -r requirements.txt
