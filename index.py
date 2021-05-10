import lucene
import search
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.store import RAMDirectory
from org.apache.lucene.index import IndexWriter
from org.apache.lucene.index import IndexWriterConfig
from org.apache.lucene.document import Document
from org.apache.lucene.document import Field
from org.apache.lucene.document import TextField
lucene.initVM(vmargs=['-Djava.awt.headless=true'])


def indexer(documents_file):
    analyzer = StandardAnalyzer()
    # creating a directory on the RAM
    directory = RAMDirectory()
    config = IndexWriterConfig(analyzer)
    writer = IndexWriter(directory, config)
    # indexing the documents
    doc = Document()
    lines = documents_file.readlines()
    length = len(lines)
    for line_number in range(length):
        # indexing document ID
        if lines[line_number].startswith(".U"):
            doc_id = lines[line_number+1].strip()
            writer.addDocument(doc)
            doc = Document()
            doc.add(Field("DocID", doc_id, TextField.TYPE_STORED))
        # indexing document description
        elif lines[line_number].startswith(".W"):
            paragraph = lines[line_number+1].strip()
            paragraph = search.stop_words(paragraph)
            doc.add(Field("DocParagraph", paragraph, TextField.TYPE_STORED))
        # indexing document title
        elif lines[line_number].startswith(".T"):
            paragraph = lines[line_number+1].strip()
            paragraph = search.stop_words(paragraph)
            doc.add(Field("DocParagraph", paragraph, TextField.TYPE_STORED))
        # indexing document keywords
        elif lines[line_number].startswith(".M"):
            paragraph = lines[line_number+1].strip()
            paragraph = search.stop_words(paragraph)
            doc.add(Field("DocParagraph", paragraph, TextField.TYPE_STORED))
    writer.addDocument(doc)
    writer.close()

    return directory, analyzer
