#necessary imports
import numpy as np
import pandas as pd
import csv
import lucene as ls
from java.io import File

#index imports
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
import org.apache.lucene.document as document

# importing beautiful soup for html scrapping
import os
from bs4 import BeautifulSoup
import requests

# default paths
path = 'adhoc.fire.en/en.docs.2011/' 
indexPath='index/'

# taking input from command line
import sys

n=len(sys.argv)
# path in en directory
if sys.argv[1]!='':
	path=sys.argv[1]

# path to index directory path
if sys.argv[2]!='':
	indexPath=sys.argv[2]

#inistialise the VM
ls.initVM()

indexPath=File(indexPath).toPath()
indexDir=FSDirectory.open(indexPath)


# we are using Standard analyser
# stop words removal from english analyzer
writerConfig=IndexWriterConfig(StandardAnalyzer(EnglishAnalyzer.ENGLISH_STOP_WORDS_SET))
writer=IndexWriter(indexDir,writerConfig)

# indexing wrt docno,title and text data
def indexNews(docno,title,text):
    doc=document.Document()
    doc.add(document.Field("DOCNO",docno,document.TextField.TYPE_STORED))
    doc.add(document.Field("TITLE",title,document.TextField.TYPE_STORED))
    doc.add(document.Field("TEXT",text,document.TextField.TYPE_STORED))
    writer.addDocument(doc)

# close the writer
def closeWriter():
    writer.close()

# FINDING THE FILE PATH
# Traverse from the root and find out if if there is any file in that folder store that path

# MAIN FUNCTION

if __name__=="__main__":
	# it goes to each file and parse the content of each tag in the file
	for root, directories, files in os.walk(path, topdown=False):
	    for name in files:
	    	# read the content of the file
	        file=open(os.path.join(root, name),'r').read()
	        # initialise the beauitful soup object
	        soup = BeautifulSoup(file, "lxml")
	        
	        # find titles of news
	        titles=soup.find_all('title')
	        title_text=' '
	        # if some title if found
	        if len(titles)>0:
	            for title in titles:
	                title_text=title.text

	        # find docno of news
	        docnos=soup.find_all('docno')
	        docno_text=' '
	        # if some docno is found
	        if len(docnos)>0:
	            for docs in docnos:
	                docno_text=docs.text

	        # find the text of the news
	        texts=soup.find_all('text')
	        text_text=' '
	        # if some news if found
	        if len(texts)>0:
	            for txt in texts:
	                text_text=txt.text
	        
	        # do the indexing
	        indexNews(docno_text,title_text,text_text.strip('\n').strip())
	# close the writer
	closeWriter()