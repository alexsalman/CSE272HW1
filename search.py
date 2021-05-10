from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.queryparser.classic import QueryParser


# a function to remove stop words from both queries and documents files
def stop_words(string):
    no_and = string.replace(" and ", " ")
    no_AND = no_and.replace(" AND ", " ")
    no_of = no_AND.replace(" of ", " ")
    no_the = no_of.replace(" the ", " ")
    no_in = no_the.replace(" in ", " ")
    no_to = no_in.replace(" to ", " ")
    no_a = no_to.replace(" a ", " ")
    no_for = no_a.replace(" for ", " ")
    no_comma = no_for.replace(", ", " ")
    no_semi = no_comma.replace("; ", " ")
    no_was = no_semi.replace(" was ", " ")
    no_as = no_was.replace(" as ", " ")
    no_at = no_as.replace(" at ", " ")
    no_are = no_at.replace(" are ", " ")
    no_were = no_are.replace(" were ", " ")
    no_that = no_were.replace(" that ", " ")
    no_slash = no_that.replace("/", "")
    no_stop_words = no_slash
    return no_stop_words


# main search algorithm function
def searcher(directory, analyzer, queries_file):
    lines = queries_file.readlines()
    length = len(lines)
    a_query = ''
    query_counter = 0
    log = open("log.txt", "a")
    for line_number in range(length):
        if lines[line_number].startswith("<num>"):
            query_id = lines[line_number][14:].strip()
        elif lines[line_number].startswith("<desc>"):
            a_query = lines[line_number+1].strip()
            a_query = stop_words(a_query)
        if a_query != '':
            # searching the index
            reader = DirectoryReader.open(directory)
            searcher = IndexSearcher(reader)
            # parse the query
            parser = QueryParser("DocParagraph", analyzer)
            query = parser.parse(a_query)
            # return 50 queries are required by the assignment
            hits = searcher.search(query, 50).scoreDocs
            # rank counter 1 through 50
            rank_counter = 1
            for hit in hits:
                result = searcher.doc(hit.doc)
                # write search result to log text file
                to_log = str(query_id)+" "+"Q"+str(query_counter)+" "+str(result.get("DocID"))+" "+str(rank_counter)+" "+str(hit.score)+" "+"Alex's"+"\n"
                log.write(to_log)
                rank_counter += 1
            query_counter += 1
            a_query = ''
    log.close()
