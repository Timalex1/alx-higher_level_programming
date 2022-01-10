#!/bin/bash
# Put the content length
curl -sI "$1"| grep Content-Length | cut -d " " -f2-
