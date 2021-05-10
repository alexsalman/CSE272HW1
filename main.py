#Running Pylucene using docker and PyCharm

import index
import search
import time

def main():
    starttime = time.time()
    # open documents and queries files
    documents_file = open('ohsumed.88-91', 'r')
    queries_file = open('query.ohsu.1-63', 'r')
    # record documents on the RAM directory
    directory, analyzer = index.indexer(documents_file)
    # search queries in the documents
    startsearchtime = time.time()
    search.searcher(directory, analyzer, queries_file)
    endsearchtime = time.time()
    searchtime = endsearchtime - startsearchtime
    print("Running time of only search:", searchtime)
    # closing files used in the algorithm
    documents_file.close()
    queries_file.close()
    endtime = time.time()
    running_time = endtime - starttime
    print("Running time of the algorithm using the HW data:", running_time)


if __name__ == "__main__":
    main()
