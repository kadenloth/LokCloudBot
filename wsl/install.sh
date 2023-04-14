#!/bin/bash
 
echo "Install dependencies"
sudo add-apt-repository ppa:mozillateam/ppa
sudo apt update
sudo apt install xserver-xephyr
sudo apt install firefox-esr
sudo apt install -y python3 python3-pip
pip install opencv-python mss pyautogui numpy matplotlib
mkdir profiles
DEFAULT_PROFILE=$(cat ~/.mozilla/firefox/profiles.ini | grep Path= | head -n 1 | cut -d "=" -f 2)
cp -r "$DEFAULT_PROFILE" ./profiles/default

echo "Install bot"
curl https://raw.githubusercontent.com/kadenloth/LokCloudBot/main/wsl/start_browser.sh -o start_browser.sh
chmod a+x start_browser.sh
curl https://raw.githubusercontent.com/kadenloth/LokCloudBot/main/wsl/bot.py -o bot.py
