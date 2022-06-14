#!/bin/bash

#Global Variables

userid=`id -u`
osinfo=`cat /etc/issue|cut -d" " -f1|head -n1`
distinfo=`cat /etc/issue|cut -d" " -f2|head -n1`
chrome='https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
chromedriver_latest='https://chromedriver.storage.googleapis.com/103.0.5060.24/chromedriver_linux64.zip'

export TERM=linux


clear

if [ "${userid}" != '0']; then
	echo '[Error]: You must run this setup with root privileges.'
	echo
	exit 1
fi

pushd . > /dev/null && cd "$(dirname "$0")"

apt-get update
echo '[*] Installing Dependencies'
apt-get install -y cmake python3 xvfb python3-pip python3-netaddr python3-dev firefox-esr
echo
echo '[*] Installing Python Modules'
python3 -m pip install undetected_chromedriver
python3 -m pip install selenium --upgrade
python3 -m pip install time
python3 -m pip install argparse
python3 -m pip install os
echo
wget ${chrome}
dpkg -i google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb
wget ${chromedriver_latest}
unzip chromedriver_linux64.zip
cp chromedriver /usr/local/bin
cd ..
