# Standalone v2 for Windows

The new version should run on Windows without any complicated setup.

## Download and setup

Download the bot `main.exe` file from https://lok.cloudbot.site/standalone-v2/download

Newest version: v2.1

Download or save the `config.json` in this repository to a file.

Edit the following fields in the `config.json` using a text editor:

* `profile`: The name of this bot profile. The name can be anything, but it should be unique per Lok Account. You can put any name to identify your kingdom or account".
* `chrome_profile_path`: The path to your Chrome profile. For using multiple accounts you will have to create different Chrome profiles. You should login in this profile before starting the bot.

> [!TIP] 
> To find the profile path being used, start Chrome in the profile and paste `chrome://version` in the url bar. The path of the profile will be shown after "Profile Path:"

* `token`: The token is your "User Token" that you see in
  https://lok.cloudbot.site/standalone. You get a free token when you create an account. You can also purchase "rounds" that you can convert to add more subscription time.
* `bot_options`: This is the configuration of your bot. See [Bot Options section](#bot-options) for more details.

## Running the bot
Once you have configured everything correctly, you can start the bot.

To run, open Windows Power Shell in the bot folder, and run:

`./main.exe config.json` or `./main.exe <path your config.json>`

You can also run it with the `-n` flag to repeat `n` times. There is also the `-w` flag to wait between runs.

`./main.exe config.json -n 10 -w 120`

The command above will run bot 10 times, waiting two minutes between runs.

## Bot Options

Here are an explanation of each option you can configure in your `config.json`.

```
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

## Running Multiple accounts

To run multiple accounts, create a new `config.json` and edit the `profile` and `chrome_profile_path` fields. 
Each account should use a different `config.json` with different `profile` name and different `chrome_profile_path`.

## Dependencies 

* Chrome - You need Chrome installed to run the game
* Tesseract - Install Tesseract if you get error saying it is not installed. [Link tesseract](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe).
> [!IMPORTANT]
> Make sure it is installed in `C:/Program Files/Tesseract-OCR/` for it to work. If not, set the installation path in the `config.json` adding `"tesseract_path":<path>` to the .

