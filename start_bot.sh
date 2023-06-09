#!/bin/bash

if [ $# -lt 1 ]; then
	echo 'Usage: ./start_bot.sh <profile> -c <config_path>'
	exit 1
fi

PROFILE=$1
DISPLAY_NUM=$(ls -tr1 profiles/ | nl | awk -v profile="$PROFILE" '{if ($2 == profile) print $1}')

export DISPLAY=:$DISPLAY_NUM
set -e

./main.bin $@
