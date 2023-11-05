#necessary imports
import math
import numpy as np
import pandas as pd
import csv
import lucene as ls
from java.io import File
from java.io import StringReader
#index imports
# from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
import org.apache.lucene.document as document

import os
from bs4 import BeautifulSoup
import requests

import re
import sys
# Retriever imports:
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory

from org.apache.lucene.index import IndexReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search.similarities import BM25Similarity


def search(index_path,q):
	# same analyser as the indexer one
    analyzer=StandardAnalyzer()
    # make the parser
    query=QueryParser("TEXT",analyzer).parse(q)
    
    directory=FSDirectory.open(File(index_path).toPath())
    # searcher
    searcher=IndexSearcher(DirectoryReader.open(directory))
    
#     searcher.setSimilarity(BM25Similarity(k1,b))
#     by default tf-idf score ing
    scoreDocs=searcher.search(query,1000).scoreDocs
    # retrieve 100 docs
#     print(scoreDocs)
    result=[]
    # ranks
    cnt=0
    for scoreDoc in scoreDocs:
#         similarity_score=scoreDoc.score
#         print(scoreDoc.score)
        doc=searcher.doc(scoreDoc.doc)
        result.append([doc.get("DOCNO"),cnt,math.ceil(scoreDoc.score*100)/100])
        cnt+=1
    return result
#         print(doc)
#         print(doc.score)
#         return doc.get("TEXT"),doc,get("DOCNO")
#         print("name",doc.get("DOCNO"))
#         doc,get(search_field) and doc.get(field to retrieve)

if __name__=="__main__":
	# start lucene
	ls.initVM()
	index_path=''
	if sys.argv[1]!='':
		index_path=sys.argv[1]

	query_file_path='en.topics.126-175.2011.txt'
	
	if sys.argv[2]!='':
		query_file_path=sys.argv[2]
	
	file=open(query_file_path,'r')

	soup = BeautifulSoup(file, "lxml")

	# retrieve the documents
	titles=soup.find_all('title')
	desc=soup.find_all('desc')
	query=soup.find_all('num')

	outputDir=''
	if sys.argv[3]!='':
		outputDir=sys.argv[3]
	# handle if the folder is already created
	try:
		os.mkdir(outputDir)
	except OSError as error:
		print("A folder already exits")

	outputfilePath=outputDir+'output1.txt'
	# file=open(outputfilePath,'a')
	output=open(outputfilePath,'w');output.close()

	# title only
	for item in range(len(titles)):
	    result=search(index_path,titles[item].get_text())
	    for _ in range(len(result)):
	        col=[query[item].get_text(),'Q0']
	        col.extend(result[_]);col.append('mtc2109')
	        col=np.array([col])
	        with open(outputfilePath,'a',newline='') as output:
	            mywriter=csv.writer(output,delimiter=' ')
	            mywriter.writerows(col)

	file.close()

	# text +description
	outputfilePath2=outputDir+'output2.txt'
	output2=open(outputfilePath2,'w');output2.close()
	for item in range(len(titles)):
	    result=search(index_path,titles[item].get_text()+desc[item].get_text())
	    for _ in range(len(result)):
	        col=[query[item].get_text(),'Q0']
	        col.extend(result[_]);col.append('mtc2109')
	        col=np.array([col])
	        with open(outputfilePath2,'a',newline='') as output2:
	            mywriter=csv.writer(output2,delimiter=' ')
	            mywriter.writerows(col)


# the program writes only in file