#Running Pylucene using docker and PyCharm

import index
import search


def main():
    # open documents and queries files
    documents_file = open('ohsumed.88-91', 'r')
    queries_file = open('query.ohsu.1-63', 'r')
    # record documents on the RAM directory
    directory, analyzer = index.indexer(documents_file)
    # search queries in the documents
    search.searcher(directory, analyzer, queries_file)
    # closing files used in the algorithm
    documents_file.close()
    queries_file.close()


if __name__ == "__main__":
    main()
