# Lizzie Tonkin
# Multiprocessing processing of fastq files
# Bigelow Internship, 2014


# Important Import Stuff
import multiprocessing
from itertools import izip_longest


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
	data =  file(filename, 'rU').readlines()
	for chunk in grouper(data, 4):
		chunky = [chunk[0].strip("\n"),chunk[1].strip("\n"),chunk[3].strip("\n")]
		yield chunky


# Maine function
if __name__ == '__main__':
	
	p = multiprocessing.Pool(4)
	
	for name, seq, qual in makeFASTQGenerator("test.fastq"):
		print name
		print seq
		print qual
		print ""
	
#	results = p.map(process_chunk, makeFASTQGenerator("test.fastq"))
#	print results

