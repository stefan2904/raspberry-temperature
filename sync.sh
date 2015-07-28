#!/bin/bash

tail -n 1 temp_log.csv | ssh -o ConnectTimeout=30 home "cat >> /var/www/camp/temp/temp_log.csv"
