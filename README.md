# Standalone v2 for Windows

The new version should run on Windows without any complicated setup.

## Download and setup

Download the bot `main.exe` file from https://lok.cloudbot.site/standalone-v2/download

Newest version: v2.0.3

Download or save the `config.json` in this repository to a file. 

Edit the following fields in the `config.json` using a text editor:

* `profile`: The name of this bot profile. The name can be anything, but it should be unique per Lok Account. You can put any name to identify your kingdom or account".
* `chrome_profile_path`: The path to your Chrome profile. For using multiple accounts you will have to create different Chrome profiles. You should login in this profile before starting the bot.

> [!TIP] 
> To find the profile path, start Chrome in the profile and paste `chrome://version` in the url bar. The path of the profile will be shown after "Profile Path:"

* `token`: The token is your "User Token" that you see in
  https://lok.cloudbot.site/standalone. You get a free token when you create an account. You can also purchase "rounds" that you can convert to add more subscription time.
* `bot_options`: This is the configuration of your bot. Configure it depending on what you want the bot to do (e.g. mine resources, build castle, attack monsters).

## Running the bot
Once you have configured everything correctly, you can start the bot.

To run, open Windows Power Shell in the bot folder, and run:

`./main.exe config.json` or `./main.exe <path your config.json>`

You can also run it with the `-n` flag to repeat `n` times. There is also the `-w` flag to wait between runs.

`./main.exe config.json -n 10 -w 120`

The command above will run bot 10 times, waiting two minutes between runs.


## (Advanced) Multiple accounts

To run multiple accounts, you can simply clone your Chrome profile and create a new `config.json`.

## Dependencies 

* Chrome - You need Chrome installed to run the game
* Tesseract - Install Tesseract if you get error saying it is not installed. [Link tesseract](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe).
> [!IMPORTANT]
> Make sure it is installed in `C:/Program Files/Tesseract-OCR/` for it to work.

