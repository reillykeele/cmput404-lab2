#!/bin/bash

# make sure to kill this process after 
python3 echo_server.py &

sleep 1

echo "Foobar" | nc localhost 8001 -q 1 & 
echo "Foobar" | nc localhost 8001 -q 1 & 
echo "Foobar" | nc localhost 8001 -q 1 & 