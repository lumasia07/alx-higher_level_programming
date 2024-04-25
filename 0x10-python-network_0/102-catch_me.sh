#!/bin/bash
# Message in response server
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchoool" 0.0.0.0:5000/catch_me
