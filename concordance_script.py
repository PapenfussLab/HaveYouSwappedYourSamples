#!/usr/bin/env python

import sys

	
def read_file(file):
	f = open(file)
	snps = []
	for l in f.readlines():
		try:
			snp = l.split()[0]
			freq = float(l.split()[3])
			snps.append((snp, freq))
		except ValueError:
			 print "line %s produces value error when parsing frequency in file %s! SKIPPING VARIANT." %(l, file)
	f.close()
	return snps

def next_variant(list, index):
	index += 1
	if index < len(list):
		s,f = list[index]
		return index , s, f
	else :
		return index, "", 0

def concordance(sample, germline, symmetrical, homo_threshold, hetero_threshold):
	i=j=-1
	i, snp1, f1 = next_variant(sample, i)
	j, snp2, f2 = next_variant(germline, j)
	concordant = 0
	discordant = 0
	while i<len(sample) and j<len(germline):
		if snp1==snp2:
			if f2 >= homo_threshold:
				if f1 >= homo_threshold:
					concordant += 1
				else :
					discordant += 1
			elif f1 >= homo_threshold:
				if symmetrical:
					discordant += 1
			i, snp1, f1 = next_variant(sample, i)
			j, snp2, f2 = next_variant(germline, j)
		elif snp1 < snp2:
			if f1 >= homo_threshold and symmetrical or f1 >= hetero_threshold and not symmetrical:
				discordant += 1
			i, snp1, f1 = next_variant(sample, i)
		else:
			if f2 >= homo_threshold:
				discordant += 1
			j, snp2, f2 = next_variant(germline, j)
	while i < len(sample):
		if f1 >= homo_threshold and symmetrical:
			discordant += 1
		i, snp1, f1 = next_variant(sample, i)
	while j < len(germline):
		if f2 >= homo_threshold:
			discordant += 1
		j, snp2, f2 = next_variant(germline, j)
	return concordant, discordant
		

def calculate_concordance(samples, germlines, symmetrical, output):
	sam = open(samples).read().splitlines()
	out = open(output, 'w')
	
	all_samples = {}
	for s in sam:
		all_samples[s] = read_file(s)
	if samples == germlines:
		all_germlines = all_samples
		germ = sam
	else:
		germ = open(germlines).read().splitlines()
		all_germlines = {}
		for g in germ:
			all_germlines[g] = read_file(g)
	
	for s in sam:
		sample = all_samples[s]
		for g in germ:
			germline = all_germlines[g]
			c,d = concordance(sample, germline, symmetrical, 0.9, 0.4)
			out.write("%s\t%s\t%1.3f\t%d\n" %(s, g, float(c)/(c+d), c+d)) 
	out.close()




if len(sys.argv) < 4:
	print "Usage: [options] <samples> <germ lines> <concordance output>\n",\
				"Options: \n\t-s: Symmetrical evaluation (consider homzygotes from sampels and germ lines\n",\
				"\t\talike. By default only germ line SNPs are regarded\n"

	sys.exit(0)

i=1
symmetrical = False
heat = None
while i < len(sys.argv)-3:
	if sys.argv[i] == "-s":
		symmetrical = True
		i += 1
	else :
		print "Unknown option: %s. Exiting." %(sys.argv[i])
		sys.exit(0)



calculate_concordance(sys.argv[i], sys.argv[i+1], symmetrical, sys.argv[i+2])
