#!/usr/bin/env python3
#coding=utf-8

import os
import re
import collections 
import argparse 
import json


#Creation of arguments for command lines interface
parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('--fileToRead', dest='fileToRead', help='Name of the file the program must analyse')
parser.add_argument('--resultFile', dest='resultFile', help='Name of the file to contain the results')
parser.add_argument('--inputDir', dest='inputFile')
parser.add_argument('--outputDir', dest='outputFile')
args = parser.parse_args()

def main():

	dic = {}   #Creation of the dictionnary
	words=re.findall('\w+',open('fileToRead.txt').read().lower()) #find words in text
	dic =collections.Counter(words) #elements are stored as dictionary keys and their counts are stored as dictionary values
	for i in dic.keys():
		dic[i]/=len(words)   #putting in frequency
		with open('result.json','w') as fileopen : 
			json.dump(dic ,fileopen,indent=2) #indent=2 go to line    json format
			

if __name__=='__main__' :
		main()

