#!/usr/bin/env sh

while [ 1 -eq 1 ]; do
	date
	python linebot.py --mode room --target all --execute
	sleep 10 
done
