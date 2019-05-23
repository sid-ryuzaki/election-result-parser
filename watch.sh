#!/bin/bash
ARGS="${@}"
clear; 
while(true); do 
  OUTPUT=`$ARGS`
  clear
  echo -e "$(date)"
  echo -e "${OUTPUT[@]}"
  sleep 10
done
