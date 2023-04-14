#!/bin/bash

echo "Update bot"
curl https://raw.githubusercontent.com/kadenloth/LokCloudBot/main/wsl/start_browser.sh -o start_browser.sh
chmod a+x start_browser.sh
curl https://raw.githubusercontent.com/kadenloth/LokCloudBot/main/wsl/bot.py -o bot.py
