#!/bin/bash

if ! [ $(id -u) = 0 ]; then
    echo "run this in root"
exit 1
fi


echo "removing all the EEEVVVVVIIIILLLLLL"

sudo apt purge nmap
sudo apt purge wireshark-graphical
sudo apt purge wireshark-cli
sudo apt purge ettercap-graphical
sudo apt purge ettercap-cli
sudo apt purge netcat

echo "script has finished purging, bye bye"
