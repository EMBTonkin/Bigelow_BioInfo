import multiprocessing
from itertools import izip_longest

def process_chunk(chunk):
	#Just a silly function which proves this is doing something by taking the name of the sequence and adding a know fact to it,
	return chunk[0]+ "Lizzie is cool"

def grouper(iterable, n, fillvalue=None):
    # "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def makeFASTQGenerator(filename):
	data =  file(filename, 'rU').readlines()
	for chunk in grouper(data, 4):
		chunky = [chunk[0].strip("\n"),chunk[1].strip("\n"),chunk[3].strip("\n")]
		yield chunky

if __name__ == '__main__':
	
	p = multiprocessing.Pool(4)
	
	for name, seq, qual in makeFASTQGenerator("test.fastq"):
		print name
		print seq
		print qual
		print ""
	
#	results = p.map(process_chunk, makeFASTQGenerator("test.fastq"))
#	print results

