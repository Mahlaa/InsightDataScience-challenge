import sys
from math import floor


def median_unique(file_in):
	file_out2 = open ("./tweet_output/ft2.txt" , "w")
	dicts = []
	counts = []
	medians = []
	for lin in file_in.readlines():
		if lin == "\n":
			continue
		tweet_dic = dict()
		for item in lin.split():
			if item in tweet_dic:
				tweet_dic[item] = tweet_dic[item] + 1
			else:
				tweet_dic[item] = 1
		dicts.append (tweet_dic)		
		
	for item in dicts:
		count = 0
		for elem in item:
			count = count + 1
		counts.append (count)
	
	medians.append(counts[0])
	for i in range(1,len(counts)):
		if (i%2 != 0):
			medians.append((counts[floor(i/2)] + counts[floor(i/2)+1]) /2)
		else:
			medians.append(counts[floor(i/2)])
	
	for item in medians:
		file_out2.write(str(item) + "\n")
			

def main(argc , argv):
	if argc<2 or argv[1][-4:] != '.txt':
		sys.exit('Usage: python words_tweeted.py tweets.txt ft1.txt')
	try:
		file_in = open(argv[1] , 'r')
	except IOError:
		sys.exit('Input file missing')

	median_unique(file_in)

if __name__ == "__main__":
	main(len(sys.argv) , sys.argv)



