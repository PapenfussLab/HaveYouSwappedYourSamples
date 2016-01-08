# HaveYouSwappedYourSamples
This project contains simple methods to measure sample relatedness and identify potential swaps and contamination


------------
INSTALLATION
------------
Clone the repository for the latest version:
	git clone http://github.com/PapenfussLab/HaveYouSwappedYourSamples.git
There are some dependencies to the modules:
- HaveYouSwappedYourSamples.sh: None.
- concordance_script.py (calculate concordance module): Python.
- plotting_script.R (plot a heat map): The optional plotting routine depends on ggplot2 being installed within R.
- model_analysis.py (calculate Gaussian micture model): This optional module relies on Python and the Python libraries sklearn.mixture, numpy, and scipy.
----
DATA
----
The tool relies on the data being formatted and sorted in the following way:  
1. each sample (and germ line) should have one tab delimited file that specifies  
    SNP_ID CHR POS VAF  
    The script actually only uses the VAF field (variant allele frequency)  
2. the files specified above have to be lexicographically sorted by SNP_ID and SNP_IDs have to be unique within a sample.
Specify the absolute path to each of the files in a text file (one row per file)  
Germ lines and samples should be specified in separate files.  

-----
USAGE
-----
Run the "HaveYouSwappedYourSamples.sh" script followed by a module identifier:  
	"conc"
	"heat"
	"model"
Each module needs optional and mandatory parameters:
1. conc
	-s (OPTIONAL): Symmetrical evaluation (consider homzygotes from samples and germ lines
			alike. By default only germ line SNPs are regarded
	<FILE>: The file with paths to the samples
	<FILE>: The file with paths to the gern lines (or samples, if an all vs. all concordance test is desired (use together with -s option).
2. heat
	<FILE>: The file with the concordance measures (as produced by the "conc" module).
	<FILE>: An output pdf file for the heat map to be saved as.
3. model
	<FILE>: The file with the concordance measures (as produced by the "conc" module).
