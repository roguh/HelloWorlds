#!/bin/sh
HOST=http://127.0.0.1:5000
curl -H "Content-Type: application/json" -d '{"recipient":"earthling"}' $HOST/to-recipient
