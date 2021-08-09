#!/bin/bash

file='index.html'
echo "Updating file: $file" 
sed -i "" "s/.*last updated.*/last updated $(date '+%F')/g" $file


file='publications/index.html'
echo "Updating file: $file" 
sed -i "" "s/.*last updated.*/last updated $(date '+%F')/g" $file



file='resume/index.html'
echo "Updating file: $file" 
sed -i "" "s/.*last updated.*/last updated $(date '+%F')/g" $file


file='research/index.html'
echo "Updating file: $file" 
sed -i "" "s/.*last updated.*/last updated $(date '+%F')/g" $file
