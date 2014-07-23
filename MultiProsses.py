import multiprocessing
from itertools import izip_longest
 
def process_chunk(d):
	#Just a silly function which proves this is doing something by taking the name of the sequence and adding a know fact to it,
	return d[0]+ "Lizzie is cool"
 
def grouper(iterable, n, fillvalue=None):
    # "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)
 
if __name__ == '__main__':
 
	test_data = file("test.fastq", 'rU').readlines()
	
	p = multiprocessing.Pool(4)
 	
	chunks = []	
	for chunk in grouper(test_data, 4):
		chunks.append(chunk)
	
	results = p.map(process_chunk, chunks)
	print results
