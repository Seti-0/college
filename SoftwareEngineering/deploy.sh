#!/bin/bash
# This script is deprecated now, but auto-deploy script used to launch scrapers in sprint 1

echo "Killing python scripts to redeploy updated scripts from Git"

# Kill current scripts
pkill -f stations_scraper.py
pkill -f bikes_scraper.py

echo "Fetching updated Git repo"
# Pull will fetch and merge in a single command
# origin is the result of git remote -v (git@github.com:TitanicProductions/DublinBikesSE.git)
git pull origin main

echo "Restarting scripts"
# Restart python scripts in background  with no hangup
nohup python3 bikes_scraper.py </dev/null &>/dev/null &
nohup python3 weather_scraper.py </dev/null &>/dev/null &
