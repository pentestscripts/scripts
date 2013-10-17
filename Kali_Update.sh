#!/bin/bash

clear

echo -e "\e[1;36mKali Update Script\e[0m"

echo "Press ENTER to continue, CTRL+C to abort."
read input

echo -e "\e[1;36m[+] Updating Kali. Please wait.\e[0m"
apt-get update -y > /dev/null && apt-get upgrade -y > /dev/null && apt-get dist-upgrade -y > /dev/null
echo -e "Kali is now up to date.\n"

echo -e "\e[1;36m[+] Cleaning Kali. Please wait.\e[0m"
apt-get autoclean -y > /dev/null && apt-get clean -y > /dev/null
echo -e "\e[1;36m[+] Kali is now less dirty...Giggity\e[0m"
