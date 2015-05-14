#!/bin/bash
head -n 1 trip_merged_1.csv > final_merged.csv

for i in 1 2 3 4 5 6 7 8 9 10 11 12
do
shuf -n 1000000 trip_merged_$i.csv >> final_merged.csv
done
