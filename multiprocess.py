#!/usr/bin/env python
# coding=utf-8
"""
Lizzie Tonkin
Multiprocessing of fastq files
Bigelow Internship, 2014
"""

# Important Import Stuff
import sys
import multiprocessing
from itertools import islice, izip_longest


def read_fastq(fq):
    # add gzip support here
    with open(fq) as fh:
        #
        fqclean = (x.strip("\r\n") for x in fh if x.strip())
        while True:
            #
            r = [x for x in islice(fqclean, 4)]
            #
            if not r: raise StopIteration
            #
            assert all(r) and len(r) == 4
            #
            yield r[0][1:], r[1], r[3]


# does not do anything useful now, but soon it will do useful things to the records and return those useful things
def process_chunk(chunk):
	return chunk[0]+ "Lizzie is cool"

# Groups the input into hunks of four
# returns a tuple
# code directly copied off the python site
def grouper(iterable, n, fillvalue=None):
    # "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

# Creates a generator which returns a list containing the three useful lines per fastq record
# filename: string, name of the fastq file
# returns generator, which yields three element lists containing the important parts of each fastq record.
def makeFASTQGenerator(filename):
	with open(filename, 'rU') as f:
		for i in range(5):
			fifth = f.readline()
        # empty lines may be sporadic, so this will fail
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
    """as an example, docstrings go here.
    validates records by making sure all three parts of the record exist
    filename: string, name of the fastq file
    returns boolean: true if the records in the file are valid, false of not.
    """
	for record in makeFASTQGenerator(filename):
		for part in record:
			if part.isspace() or (part == ""):
				return False
	return True


def main(fastq):
    # for name, seq, ... etc

    # calculate GC content as a percent of total observed sequence.
    # you need to know how many bases were present (len(sequence))
    # for each sequence, you need to count 'G' and 'C'
    # you don't have to worry about doing anything in multiprocessing yet


# Maine function
if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('test')
    args = p.parse_args()
    main(args.test)

	# check for proper amount of command line arguments
    # if len(sys.argv) < 2:
    #     print ''
    #     print 'Oi!  Inproper file usage!'
    #     print 'usage: python MultiProsses.py <filename.fastq>'
    #     print ''
    #     quit()
    #
    # # check for proper record formatting
    # if validateRecords(sys.argv[1]) == False:
    #     print ''
    #     print 'Error!  Invalid input!'
    #     print 'Something in your record is invalid.  Make sure that all parts of the record are there and formated consistently'
    #     print ''
    #     quit()
    #
    # p = multiprocessing.Pool(4)
    #
    # for name, seq, qual in makeFASTQGenerator(sys.argv[1]):
    #     print name
    #     print seq
    #     print qual
    #     print ""

#	results = p.map(process_chunk, makeFASTQGenerator("test.fastq"))
#	print results
