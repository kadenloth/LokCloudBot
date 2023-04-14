#!/bin/bash
 
sudo add-apt-repository ppa:mozillateam/ppa
sudo apt update
sudo apt install xserver-xephyr
sudo apt install firefox-esr
sudo apt install -y python3 python3-pip
pip install opencv-python mss pyautogui numpy matplotlib
mkdir profiles

curl 
