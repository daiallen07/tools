#!/bin/bash



# Extract IP addresses using regular expression
grep -oP '\b(?:\d{1,3}\.){3}\d{1,3}\b' ""
