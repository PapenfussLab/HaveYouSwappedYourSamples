#!/bin/bash

if [ -z $4 ] ; then
	echo "Usage: <samples> <germ lines> <concordance output> <one sided concordance: y/n> [heat map plot desitination]"
	exit
fi

echo -n "" > $3
if [ "$4" = "y" ] ; then
	echo "Only considering homozygots in germ lines to avoid confusion due to massive LOH."
	c=1
else
	echo "Considering all homozygots..."
	c=0
fi

echo "Starting to compare all samples vs. all germ lines"
for s in `cat $1`; do
	for f in `cat $2`; do
		echo -n $s" "$f" " >> $3
		join $s $f | awk -v c=$c 'BEGIN{sum=0; pos=0} {if($4>0.9) { if($7>0.9) { sum +=1; pos +=1;} else if(c==0) sum +=1} else if($7>0.9) sum+=1} END{print pos/sum, sum}' >> $3
	done
done


if [ ! -z $5 ] ;then
	echo "Plotting the heat map"
	R --no-save --args $3 $5 < plotting_script.R
fi

echo "Done"
	
