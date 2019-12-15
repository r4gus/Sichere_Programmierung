#!/bin/sh

if [ $# -eq 0 ]
then
	echo -e "\e[31minvalid number of arguments.\e[0m"
	echo -e "\e[36mUSAGE:\e[0m $0 <file>.tex"
fi

pdf_name=$(echo $1 | cut -d "." -f 1).pdf

if [ -f $pdf_name ]
then
	evince $pdf_name &
fi

vim $1
