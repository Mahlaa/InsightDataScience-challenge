import sys
from math import floor


def words_tweeted(file_in):
	file_out = open ("./tweet_output/ft1.txt" , "w")
	dic_total = dict()
	for lin in file_in.readlines():
		if lin == '\n':
			continue
		for item in lin.split():
			if item in dic_total:
				dic_total[item] = dic_total[item] + 1
			else:
				dic_total[item] = 1		
		
	
	dic_new = sorted(dic_total, key = lambda a: a[0])
	for item in dic_new:
		file_out.write(str(item) + "\t"+"\t"+"\t" + str(dic_total[item]) + "\n")
	
			

def main(argc , argv):
	if argc<2 or argv[1][-4:] != '.txt':
		sys.exit('Usage: python words_tweeted.py tweets.txt ft1.txt')
	try:
		file_in = open(argv[1] , 'r')
	except IOError:
		sys.exit('Input file missing')

	words_tweeted(file_in)

if __name__ == "__main__":
	main(len(sys.argv) , sys.argv)



