#!/bin/sh

if [ $# -lt 1 ]
then
	echo -e "\e[31mError:\e[0m Invalid number of arguments."
	exit 1
fi

address=$1


