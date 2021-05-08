from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.queryparser.classic import QueryParser


def searcher(directory, analyzer, queries_file):

    lines = queries_file.readlines()
    length = len(lines)
    a_query = ''
    query_counter = 0
    for line_number in range(length):
        if lines[line_number].startswith("<num>"):
            query_id = lines[line_number][14:].strip()
        elif lines[line_number].startswith("<title>"):
            a_query = lines[line_number][8:].strip().replace("/", "")
        if a_query != '':
            # now search the index
            reader = DirectoryReader.open(directory)
            searcher = IndexSearcher(reader)
            # parse a simple query that searches for "text"
            parser = QueryParser("DocParagraph", analyzer)
            query = parser.parse(a_query)
            hits = searcher.search(query, 5).scoreDocs
            for hit in hits:
                result = searcher.doc(hit.doc)
                print(query_id, " Q", query_counter, result.get("DocID"), " ", result.get("DocParagraph"))
            print('\n')
            query_counter += 1
        a_query = ''
