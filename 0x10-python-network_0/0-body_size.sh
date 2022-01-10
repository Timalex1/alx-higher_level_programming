#!/bin/bash
# Put the content length
curl -sI "" | grep Content-Length | cut -d " " -f2-
