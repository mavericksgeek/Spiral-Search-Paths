#!/bin/bash
for i in `seq 1 300`;
	do
		make; python main1.py
		sleep 2
	done    
