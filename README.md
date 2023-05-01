# dolly-llm-api

Execute following to install required libraries

### Starting a virtual env
python3 -m pip install virtualenv

virtualenv -p /usr/bin/python3 llm

source llm/bin/activate

### Installing required librraies

python3 -m pip install git+https://github.com/huggingface/transformers

python3 -m pip install accelerate>=0.12.0

python3 -m pip install flask

python3 -m pip install waitress