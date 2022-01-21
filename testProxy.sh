#!/bin/bash

# make sure to kill this process after 
python3 proxy_server.py &

sleep 1

python3 proxy_client.py > out1.log &
python3 proxy_client.py > out2.log &