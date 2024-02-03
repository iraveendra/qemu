#!/bin/bash

for script in "cpu1000.sh" "cpu2000.sh" "fileiorrw.sh" "fileioseq.sh" "mem1M.sh" "mem512K.sh"; do
	for i in 1 2 3 4 5; do
		echo "Running iteration $i of $script"
		./$script >> log_${script%.*}_$i.txt
		echo "Iteration $i of $script done"
	done									done
echo "All done"
