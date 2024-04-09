from collections import Counter
def count(fname):
    	with open(fname) as f:
            	return Counter(f.read().split())

print("Frequency of words in the file :",count("test.txt"))
