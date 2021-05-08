import lucene
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.store import RAMDirectory
from org.apache.lucene.index import IndexWriter
from org.apache.lucene.index import IndexWriterConfig
from org.apache.lucene.document import Document
from org.apache.lucene.document import Field
from org.apache.lucene.document import TextField
lucene.initVM(vmargs=['-Djava.awt.headless=true'])
print(lucene.VERSION)


def indexer(documents_file):
    analyzer = StandardAnalyzer()
    directory = RAMDirectory()
    config = IndexWriterConfig(analyzer)
    writer = IndexWriter(directory, config)

    # indexing the documents
    doc = Document()
    lines = documents_file.readlines()
    length = len(lines)
    for line_number in range(length):
        if lines[line_number].startswith(".I"):
            doc_id = lines[line_number][3:].strip()
            writer.addDocument(doc)
            doc = Document()
            doc.add(Field("DocID", doc_id, TextField.TYPE_STORED))
        elif lines[line_number].startswith(".W"):
            paragraph = lines[line_number+1].strip()
            doc.add(Field("DocParagraph", paragraph, TextField.TYPE_STORED))
    writer.addDocument(doc)
    writer.close()

    return directory, analyzer
