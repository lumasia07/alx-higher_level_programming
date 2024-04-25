#!/bin/bash
# Displays a response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
