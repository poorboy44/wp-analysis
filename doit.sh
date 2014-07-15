#!/usr/bin/env bash
filelist=$(find /mnt2/archives/wp-com/2014/ -name "*.gz" )
rm -rf ~/summary.csv ~/matched_activities.json unzipped.txt
for arg in $filelist
do
	gzip -cd $arg > ~/unzipped.txt
	jruby powertraq_interpreter_lite.rb -m --publisher wordpresscom -r ~/dnbq.rules -a ~/unzipped.txt > ~/matched_activities.json
	python ~/summarize.py
done
