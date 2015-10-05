# HaveYouSwappedYourSamples
This project contains simple methods to measure sample relatedness and identify potential swaps and contamination


------------
INSTALLATION
------------
The main script (concordance_script.sh) only depends on the right kind of data and bash.  
The optional plotting routine depends on ggplot2 being installed within R.  

----
DATA
----
The script relies on the data being formatted and sorted in the following way:  
1. each sample (and germ line) should have one tab delimited file that specifies  
    SNP_ID CHR POS VAF  
    The script actually only uses the VAF field (variant allele frequency)  
2. the files specified above have to be lexicographically sorted by SNP_ID  
Specify the absolute path to each of the files in a text file (one row per file)  
Germ lines and samples should be specified in separate files.  

-----
USAGE
-----
Run the "concordance_script.sh" script.  
Specify (i) the file containing the sample files,  
(ii) the file containing the germ line files (if no germ lines are available, or  
    all samples are to be compared against each other, this can be the same as (i)),  
(iii) the destination file for the output of the script,  
(iv) a binary switch (y/n) to indicate if homozygotes in both samples and germ lines (n)  
    or only those in the germ lines (y) should be considered.  
		The latter option is preferrable if large LOH events are expected in the data;
and (iv) [optional] a file name for the heat map to be plotted (this may not be feasible  
    for a very large cohort, but should be intelligble with up to 100 samples).  
The file specified in (iii) contains 4 columns:  
    The file name of the first sample, the file name of the second sample (or germ line),  
    the agreement of homozygous SNPs, and the number of SNPs considered homozygous.  
The optional heat map visualises the same data.  


