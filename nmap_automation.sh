#!/bin/bash
#get ip from ping sweep
nmap -sn -iL iplist.txt -oG foundIp.txt; grep -v Down foundIp.txt; grep -oP '\b(?:\d{1,3}\.){3}\d{1,3}\b' foundIp.txt > foundIp_filtered.txt
rm iplist.txt -y
rm foundIp.txt -y
echo "Ping sweep complete"

#use ip from previous output and conduct basic nmap scan with xml and nmap format output
nmap -sC -sV -iL foundIp_filtered.txt -p- -Pn -oN nmap_output -oX xml_ouput
echo "Nmap complete"

#convert xml into HTML
xsltproc scan.xml > scan.html
echo "html file created"
