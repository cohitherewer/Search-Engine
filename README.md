Download the FIRE english corpus, query file, and relevance judgments from the below urls:

Collection Path:

https://u.pcloud.link/publink/show?code=XZCct0VZEv4mQmBGXxRGeLAznopP1z9ti8EV

Query Path:
https://www.isical.ac.in/~fire/data/topics/adhoc/en.topics.126-175.2011.txt 

Qrel Path: 
http://www.isical.ac.in/~fire/data/qrels/adhoc/en.qrels.126-175.2011.txt.gz


1. Write a program to index the FIRE english document collection using StandardAnalyzer. 

2. Write a program that takes a FIRE query file as input and creates a ranked list of 1000 documents for each query. Additionally, use the description of the query along with the query terms to search over the collection. Your program should take a string (either "onlyquery" or "querywithdesc") to expand the queries and search over the collection.

The results need to be printed in TREC format (<query number> Q0 <document id> <rank> <similarity score> <rollno>). Use Lucene's default scorer to rank the documents. 


INSTRUCTIONS: 

1. indexer.py => indexing the FIRE english document collection using StandardAnalyser
2. searcher.py => program that takes FIRE quert file as input and creates ranked list of 1000 dicuments for each query.

The result is in TREC format(<query number> Q0 <document id> <rank> <similarity score> <rollno>). I used Lucene's default scorer to rank the documents.

Note: This Repo is no longer maintained. Use it at your own risk. 
