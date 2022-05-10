#!/bin/bash

#########################################################
#  __                    , _                            #
# / ()      ,   _       /|/ \ ,_  o      _|_   ,  |)    #
# >-   |/\_/ \_/ \_/|/|  |__//  | | /|/|  |   / \_|/\   #
# \___/|_/  \/ \_/  | |_/|      |/|/ | |_/|_/o \/ |  |  #
#     (|                                                #
#########################################################

#Simple script that takes an IP address as argument and lets
# you print and then cut off whatever you can type

if [[ $# -eq 0 ]] ; then
    echo 'please provide a valid IP address as paramter'
    exit 0
fi


if [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Valid Ip address provided, opnening connection"
else
    echo 'please provide a valid IP address as paramter'
    exit 0
fi

echo "Anything you type will be printed, including nextlines"
echo "Press ctrl+c in order to cut the label"
netcat $1 9100
echo -e "\x1B@\x1DV1" | nc $1 9100
exit 0