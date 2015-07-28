#!/bin/bash

#github sync:
git add -f temp_log.csv 
git commit -m "added data"
git push

# ssh sync:
#tail -n 1 temp_log.csv | ssh -o ConnectTimeout=30 home "cat >> /var/www/camp/temp/temp_log.csv"
