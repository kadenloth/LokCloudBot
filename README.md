# Installation on Windows

## Install Debian on Windows (WSL2)

Click start menu and search for `powershell`

Open powershell and type `wsl --install -d Debian` to install.

If you need help, follow the official Microsoft documentation here https://learn.microsoft.com/en-us/windows/wsl/install

### Reboot your PC
Reboot is needed to complete the installation. After you reboot, it will show the WSL window with the instalation. Wait for it to complete.
It will ask you to create a new username and password. You can select any username and password, but make sure you remember the password.

## Opening WSL
You need to first open WSL via powershell by typing `wsl` or via start menu. If you have other WSL distros, start by running `wsl -d Debian`. 
This is required so that the bot runs in an isolated machine and doesn't interfere with your normal usage (e.g. move mouse, click, drag).

After you start WSL, you should see a terminal with your username and PC name in green (e.g. `myuser@DESKTOP:~$`). 

## Install bot and dependencies
Now, in your terminal, follow the instructions below for the Debian installation.

# Installation on Debian
The bot runs natively on the Debian/Linux OS. If you use Windows, always follow the instructions in your WSL Debian terminal.

## Install required packages
Run the following commands to install required packages:

TIP: To paste on shell, just right click.

```
sudo apt update
sudo apt install firefox-esr xserver-xephyr openbox git xdotool tesseract-ocr
```

## Clone this git repository

Run the following command to clone the bot directory, to be able to run on your PC. The command will download all files in a new folder `LokCloudBot` and save in the current directory.
```
git clone https://github.com/kadenloth/LokCloudBot.git
```

# Running the bot

## Select the bot directory
Before you run the bot, make sure you are in the git cloned repository. To do that, just `cd` into the git directory.
```
cd LokCloudBot
```

TIP: When you run `ls` to list files, you should see the `start_bot.sh` and `start_browser.sh`, which are the scripts used to run the bot.

## Start the game
To start the game, run the following command:

```
./start_browser.sh default
```

This will open an isolated Firefox window using the default profile stored in `profiles/default`.

## Add the token to your config 
To run the bot, you need a valid user token. The token can be obtained in https://lok.cloudbot.site/standalone.

Once with the token, edit the `configs/config_example.json` file. You can also edit other bot options as you like, for more info see the [Bot configuration](#bot-configuration) section.

## Run the bot
To run the bot, simply select the profile and the config. If you are using the `default` profile and the `configs_example.json` config, run the following command:

`./start_bot.sh default --config_path configs/config_example.json` 

To make the bot wait and repeat multiple times, you can pass the `-n <repeat_times>` parameter.

`./start_bot.sh default --config_path configs/config_example.json -n 10` 

## (Windows-only) Fix WSL display issue 
If you get the following error trying to start the bot:
```
Xlib.error.DisplayConnectionError: Can't connect to display ":1": [Errno 111] Connection refused
```
, then you will need to run the following command every time you reboot WSL.

```
./fix_display.sh
```

This is to fix a known issue in WSL, see https://github.com/microsoft/WSL/issues/9303

## Other common issues
### Firefox does not start
If you get the following error when you start browser:
```
Xephyr cannot open host display. Is DISPLAY set?
```
A few things you might try:

* Run `openbox` and see if you get similar issue, or command not found issue.
* Reinstall `openbox` using `sudo apt install openbox`
* Reboot host PC and try to install bot and dependencies again.

### Firefox opens, but image is scrambled
A reboot should fix this. See more info https://askubuntu.com/questions/1494619/wsl2-graphical-application-display-issue

### Other issues
If you are using Ubuntu or other Linux distros, package names might be different and bot is not guaranteed to work.

### Need help?
If you still have issues and need help, try the `#support` chat in Discord.

# Bot Configuration

You can create multiple config files for the same or multiple accounts. Just copy the `config_example.json` and edit the profile name and options. The command to copy is `cp configs/config_example.json configs/<name_of_config>.json`. To help you edit the configuration, here is an explanation of every field in the bot config json file.

TIP: To edit on Linux command line, run `nano config/config_example.json` to edit, make the changes, then press `ctrl + o` to save and `ctrl + x` to exit.

```
"profile":"default", # name of profile to be used in the logs and to store timers
"token":"<USER_TOKEN>", # your token

"auto_reconnect":true, # if enabled and the game starts in the login screen, the bot will try to login
"google_login":false, # will try to login using Google button
"email":"<optional email>" , # email to try to login via the email button
"password":"<optional password>", # password to try to login via the email button

"bot_options":{
	"build":false, # will try to upgrade buildings
	"research": false, # will try to upgrade research
	"train":false, # will try to train the last selected troop type
	"use_inventory": false, # will use items in inventory to meet requirements to upgrade buildings or research

	"gather_food":false, # will gather food mines
	"gather_wood":false, # will gather wood mines
	"gather_stone":false, # will gather stone mines
	"gather_gold":true, # will gather gold mines
	"gather_crystal":true, # will gather crystal mines
	"gather_min_level": 3, "gather_max_level": 8, # ignore mines outside this level range 
	"skip_saturday":false, # will skip gathering on saturdays (possible kill-event)

	"monsters":true, # will attack monsters
	"monster_min_level":2, "monster_max_level":4, # will ignore monsters outside this level range

	"rally":true, # will check for any alliance rally in progress and join
	"use_spells":false, # will use spells "increase resource production", "instant harvest", "accelerate gathering" if available.
	"use_boosts":false, # will use 8h boosts to increase resource production and gathering
	"alliance_donate":true, # will try to donate to alliance if there is a recommended technology
	"caravan_buy_resources":false # will buy resources and vip points from caravan using resources (not crystals)
}
```

# (Optional) Advanced Setup
## Setup multiple accounts
If you want to run multiple accounts, you need to use different browser profiles. In the `profiles/` folder inside the git directory, there is a default profile. To create another profile, just copy the default profile. The command to copy is shown below.

TIP: You can name profiles after the accounts that will run on them.

```
cp -r profiles/default profiles/my_account_1
```

To select which profile you want to start, replace `default` with your profile name. This allows you to run multiple accounts at the same time. Use the same profile for the bot, so that it connects to the correct client window. 

Example: `./start_browser.sh my_account_1` and `./start_bot.sh my_account_1 --config_path <config file>`

## Schedule or customize when to run
Ideally, you shouldn't keep the account logged in for many hours in a row running the bot in repeat mode. It is better to schedule the runs or add some pause between runs. Here is an example of script that will pause for 2 hours.

```
#!/bin/bash

while true # Repeat forever
do
    # Start browser in background
    ./start_browser.sh <profile>
    # Run bot
    ./start_bot.sh <profile> --config_path <config_file>

    # Kill browser after bot finishes
    pkill -fe "leagueofkingdoms.com"

    # Sleep for two hours (7200 seconds)
    sleep 7200
done
```
