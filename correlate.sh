#!/bin/bash

if [ -z $3 ] ; then
	echo "Usage: <samples> <germ lines> <correlated output> [heat map plot desitination]"
	exit
fi

echo -n "" > $3

echo "Starting to correlate all samples vs. all germ lines"
for s in `cat $1`; do
	for f in `cat $2`; do
		echo -n $s" "$f" " >> $3
		join $s $f | awk 'BEGIN{sum=0; pos=0} {if($4>0.9) {sum+=1; if($7>0.9) pos +=1;} else if($7>0.9) sum+=1} END{print pos/sum, sum}' >> $3
	done
done


if [ ! -z $4 ] ;then
	echo "Plotting the heat map"
	R --no-save --args $3 $4 < plotting_script.R
fi

echo "Done"
	
