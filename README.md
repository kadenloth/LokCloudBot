# Installation on Windows

## Install Debian on Windows (WSL2)

Click start menu and search for `powershell`

Open powershell

Type `wsl --install -d Debian` to install.

If you need help, follow the official Microsoft documentation here https://learn.microsoft.com/en-us/windows/wsl/install

### Reboot your PC
Reboot is needed to complete the installation. After you reboot, it will show the WSL window with the instalation. Wait for it to complete.
It will ask you to create a new username and password. You can select any username and password, but make sure you remember the password.

## Opening WSL terminal in the user directory
You can open WSL via powershell by typing `wsl` or via start menu. If you have other WSL distros, start by running `wsl -d Debian`. 

After you start WSL you should see your username and PC name in green (e.g. `myuser@DESKTOP:~$`). Make sure you are in the home directory (`~`). If it shows the `myuser@DESKTO:/mnt/wsl/...` or other path, run `cd ~` to go to the home directory. You can also start using `wsl --cd ~`

## Install bot and dependencies
Now, in your terminal, follow the instructions below for the Debian installation.


# Installation on Debian

Run the following commands to install required packages:

```
sudo apt update
sudo apt install xserver-xephyr openbox git
```

## Clone the git repository

Run the following command to clone the bot directory to be able to run on your PC.
```
git clone https://github.com/kadenloth/LokCloudBot.git
```

# Running the bot

To run the bot, just `cd` into the git directory.
```
cd LokCloudBot
```

## Start the game
After installing, you can start the game with:
`./start_browser.sh default`

This will open an isolated firefox window using the default profile.

## Add the token to your config 
To run the bot you need a valid user token. The token can be obtained in https://lok.cloudbot.site/standalone.

Once with the token, edit the `configs/config_example.json` file. You can also edit other bot options as you like, for more info see the [Bot configuration](#bot-configuration) section.

## Run the bot
To run the bot, simply select the profile and the config. If you are using the `default` profile and the `configs_example.json` config, run the following command:

`./start_bot.sh default configs/config_example.json`

# Bot Configuration

Here is an explanation of every field in the bot config json file.

```
{
	"profile":"default", # name of profile to be used in the logs
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
}
```

# (Optional) Setup for multiple accounts
If you want to run multiple accounts, you need to use different browser profiles. In the `profiles/` folder inside the git directory, there is a default profile. To create another profile, just copy the default profile. The command to copy is shown below.

Tip: You can name profiles after the accounts that will run on them.

```
cp -r profiles/default profiles/my_account_1
```

To select which profile you want to start, replace `default` with your profile name. This allows you to run multiple accounts at the same time.

Example: `./start_browser.sh my_account_1`

