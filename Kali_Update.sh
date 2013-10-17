#!/bin/bash

echo "[+] Updating Kali. Please wait."
apt-get update > /dev/null
apt-get upgrade -y > /dev/null
apt-get dist-upgrade -y > /dev/null
echo "[+] Kali Updated."
