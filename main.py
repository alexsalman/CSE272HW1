# Running Pylucene using docker
import lucene
from java.io import StringReader
from org.apache.lucene.analysis.standard import StandardAnalyzer, StandardTokenizer
from org.apache.lucene.analysis.tokenattributes import CharTermAttribute
lucene.initVM(vmargs=['-Djava.awt.headless=true'])

# tokenizer
tokenized = []
file = open('query.ohsu.1-63', 'r')
lines = file.readlines()
for line in lines:
    if line.startswith("<title>"):
        test = line[8:].strip()
        tokenizer = StandardTokenizer()
        tokenizer.setReader(StringReader(test))
        charTermAttrib = tokenizer.getAttribute(CharTermAttribute.class_)
        tokenizer.reset()
        tokens = []
        while tokenizer.incrementToken():
            tokens.append(charTermAttrib.toString())
        tokenized.append(tokens)
print(tokenized)
















# StandardAnalyzer example.
# analyzer = StandardAnalyzer()
# stream = analyzer.tokenStream("", StringReader(test))
# stream.reset()
# tokens = []
# while stream.incrementToken():
#     tokens.append(stream.getAttribute(CharTermAttribute.class_).toString())
# print(tokens)
