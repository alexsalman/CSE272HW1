# CSE272HW1

**Batch Retrieval - A Search Engine!**

Last modified 05/09/2021 23:28

## How To Implement This Algorithm:
1. Read file of documents and queries
2. Index the documents using PyLucene: StandardAnalyzer() and
RAMDirectory()
3. To start indexing, iterate through the lines of your documents, pick whatever information needed then send the content you want to use for search as a string to the stop words function so it deletes all unnecessary words that would slow down the running time and give better precision
4. After deleting unnecessary words, add the strings to a field in the RAM document
5. After adding all fields of documents, close the document writer and you will be done with the index step
6. You need to return the RAM directory and the Analyzer for the search step
7. In the search step, you will start iterating through the queries file to read and process them
8. As you did delete the stop words in the document file, you need to do the same and send your queries strings to the stop words functions to delete unnecessary words
9. After that you need to parse the queries by using QueryParser where you need to provide the field name of the document you wanna search and the analyzer
10. The next step will be scoring and ranking using the hits searched you decide (number of documents to return for each query searched)
11. The step after will be the last, writing the result into a file that has the trec format for performance evaluation
12. Using trec eval, you will get the metrics of your algorithm
