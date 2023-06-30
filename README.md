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

```
git clone
```

# Running the bot

## Start the game
After installing, you can start the game with:
`./start_browser.sh default`

## Run the bot
To run the bot you need a valid user token. The token can be obtained in https://lok.cloudbot.site/standalone.

## (Optional) Setup for multiple accounts
If you want to run multiple accounts, you need to use different browser profiles. In the `profiles/` folder inside the git directory, there is a default profile. To create another profile, just copy the default profile. The command to copy is shown below.

Tip: You can name profiles after the accounts that will run on them.

```
cp -r profiles/default profiles/my_account_1
```

To select which profile you want to start, replace `default` with your profile name. This allows you to run multiple accounts at the same time.

Example: `./start_browser.sh my_account_1`
