#!/bin/bash
# Show all methods accepted
curl -sI "$1" | grep Allow | cut -d " " -f2-
