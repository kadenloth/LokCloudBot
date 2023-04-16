# Installation

## Install WSL2
Click start menu and search for `powershell`

Open powershell

Type `wsl --install` to install.

If you need help, follow the official Microsoft documentation here https://learn.microsoft.com/en-us/windows/wsl/install

### Reboot your PC
Reboot is needed to complete the installation. After you reboot, it will show the WSL window with the instalation. Wait for it to complete.
It will ask you to create a new username and password. You can select any username and password, but make sure you remember the password.

## Opening WSL terminal in the user directory
You can open WSL via powershell by typing `wsl` or via start menu. If you have other WSL distros, start by running `wsl -d Ubuntu`. 

After you start WSL you should see your username and PC name in green (e.g. `myuser@DESKTOP:~$`). Make sure you are in the home directory (`~`). If it shows the `myuser@DESKTO:/mnt/wsl/...` or other path, run `cd` to go to the home directory. You can also start using `wsl --cd ~`

## Install bot and dependencies

Run the following command, in the home directory.

`bash <(curl -Ls https://raw.githubusercontent.com/kadenloth/LokCloudBot/main/wsl/install.sh | tr -d '\r')`
If it asks for the password, type the password you created in the previous step.

# Run 

## Starting the game and running the bot
After installing, you can start the game with:
`./start_browser.sh default`

## To run the bot, run:
`python3 bot.py default`

# Extras
## Update bot
To update the bot to a new version, run `./update.sh`

## Multiple accounts
To run multiple accounts at the same time, you need to create a new profile. You can run the following command to create a new profile:
Tip: You can name profiles after the accounts that will run on them.
`cp -r profiles/default profiles/myaccount` 
To select which profile you want to start, replace `default` with your profile name. 
Example: `./start_browser.sh myaccount`
