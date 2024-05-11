#!/bin/bash

if [ $# -lt 1 ]; then
	echo 'Usage: ./start_browser <profile>'
	exit 1
fi

PROFILE=$1
DISPLAY_NUM=$(ls -1 profiles/ | nl | awk -v profile="$PROFILE" '{if ($2 == profile) print $1}')
SCREEN_SIZE='1356x687'
if pgrep -fa "Xephyr :$DISPLAY_NUM" > /dev/null 
then
	echo "Display $DISPLAY_NUM already started"
	DISPLAY=:$DISPLAY_NUM xdotool search --name "League of Kingdoms" key ctrl+w 
	sleep 1
else
	echo "Starting browser for $PROFILE in DISPLAY:$DISPLAY_NUM"
	# Start new display
	Xephyr :$DISPLAY_NUM -softCursor -screen $SCREEN_SIZE &
	sleep 1
fi
#
export DISPLAY=:$DISPLAY_NUM
set -e

openbox &
sleep 1
#firefox --no-remote --setDefaultBrowser --kiosk https://play.leagueofkingdoms.com/
nohup firefox --kiosk --no-remote -profile profiles/$PROFILE https://play.leagueofkingdoms.com/ 2>&1 > firefox.log &
