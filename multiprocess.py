#!/usr/bin/env python
# coding=utf-8
"""
Lizzie Tonkin
Multiprocessing of fastq files
Bigelow Internship, 2014
"""

# Important Import Stuff
import argparse
import multiprocessing
from itertools import islice, izip_longest


def read_fastq(fq):
	# add gzip support here
	with open(fq) as fh:
		# Somehow removes blank lines from the file
		fqclean = (x.strip("\r\n") for x in fh if x.strip())
		while True:
			# a generator which divides the lines into groups of four
			r = [x for x in islice(fqclean, 4)]
			# if we have gotten to the end, stop
			if not r: raise StopIteration
			# Insists that records be four lines long somehow
			assert all(r) and len(r) == 4
			# yield fist, second and fourth line, where the first character of the fist line has been removed.
			yield r[0][1:], r[1], r[3]


def processChunk(chunk):
	"""Process the information in each fastq record by doing the following:
	Calculate GC content as a percent of total observed sequence.
	Results are printed right now, but will be put in a nicely formatted file at a later date.
	"""
	
	name,sequence,char=chunk
	
	# caluculate the CG %
	gc = 0.0
	for char in sequence:
		if (char == "C") or (char == "G"):
			gc += 1
	gcContent = gc / (len(sequence))
	
	#print out the lovely results in a mildly understandable way
	print name
	print "GC content is "+ str(gcContent)
	print


def grouper(iterable, n, fillvalue=None):
	"""Group the input into hunks of four.
	Return is a tuple containing the four things.
	This code is directly copied off the python site.
	"""
	# "Collect data into fixed-length chunks or blocks"
	# grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
	args = [iter(iterable)] * n
	return izip_longest(fillvalue=fillvalue, *args)


def makeFASTQGenerator(filename):
	"""Create a generator which returns a list containing the three useful lines per fastq record.
	If you have sporadic empty lines in your file, you don't deserve to have this work for you; learn to be consistent.
	filename is a string which is the name of the fastq file.
	Return a generator, which yields lists containing the three important parts of each fastq record per list.
	
	Mildly useless, since Joe made a better version
	"""
	with open(filename, 'rU') as f:
		for i in range(5):
			fifth = f.readline()
		if fifth == "\n":
			f.seek(0)
			for chunk in grouper(f.readlines(), 5):
				chunky = [chunk[0].strip("\n"),chunk[1].strip("\n"),chunk[3].strip("\n")]
				yield chunky
		else:
			f.seek(0)
			for chunk in grouper(f.readlines(), 4):
				chunky = [chunk[0].strip("\n"),chunk[1].strip("\n"),chunk[3].strip("\n")]
				yield chunky


def validateRecords(filename):
	"""Validate all records in a file by making sure all three parts of the record exist.
	filename is a string which is the name of the fastq file.
	Return a boolean, which is true if the records in the file are valid, false of not.
	"""
	for record in makeFASTQGenerator(filename):
		for part in record:
			if part.isspace() or (part == ""):
				return False
	return True
	
	
def main(fastq):
	"""Future home of awesome multiprocessing"""
	
#	if not validateRecords(fastq):
#		print "Check your input is formatted nicely"
#		quit()
	
	for record in read_fastq(fastq):
		processChunk(record)


# Maine function
if __name__ == '__main__':
	p = argparse.ArgumentParser(description=__doc__)
	p.add_argument('test')
	args = p.parse_args()
	main(args.test)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	