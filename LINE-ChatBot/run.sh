#!/usr/bin/env sh

while [ 1 -eq 1 ]; do
	date
	python linebot.py --mode contact --target 'Kinder Sung' --execute
	sleep 10 
done
