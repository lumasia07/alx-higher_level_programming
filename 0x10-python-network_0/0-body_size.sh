#!/usr/bin/bash
# Displays size of body of response of a URL
curl -s "$1" | wc -c
