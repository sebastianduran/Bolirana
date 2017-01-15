#!/bin/sh

#set here the path to the directory containing your videos
VIDEOPATH="/home/pi/bolirana/videos"

SERVICE="omxplayer --win 50,100,1230,900"

# now for our infinite loop!
while true; 
do
	if pd ax | grep -v grep | grep $SERVICE > /dev/null
	then
	sleep 1;
else
	for entry in $VIDEOPATH/*
	do
		clear
		$SERVICE $entry > /dev/null
	done
fi
done