#!/bin/bash
echo "Podaj rozszerzenie pliku źródłowego"
read rozszerzenie

echo > joinList.txt

for I in *.$rozszerzenie
do
	echo "file $I" >> joinList.txt
done

ffmpeg -f concat -safe 0 -i joinList.txt -c copy joinOutput.mkv
