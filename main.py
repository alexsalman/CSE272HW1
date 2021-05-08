#Running Pylucene using docker

import index
import search


def main():
    documents_file = open('ohsumed.88-91', 'r')
    queries_file = open('query.ohsu.1-63', 'r')
    directory, analyzer = index.indexer(documents_file)
    search.searcher(directory, analyzer, queries_file)


if __name__ == "__main__":
    main()
