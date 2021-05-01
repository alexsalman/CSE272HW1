# Running Pylucene using docker
import lucene
from java.io import StringReader
from org.apache.lucene.analysis.standard import StandardAnalyzer, StandardTokenizer
from org.apache.lucene.analysis.tokenattributes import CharTermAttribute
from collections import defaultdict
lucene.initVM(vmargs=['-Djava.awt.headless=true'])


# indexer
def indextionization(step_one):
    index = defaultdict(list)
    for i, tokens in enumerate(step_one):
        for token in tokens:
            index[token].append(i)
    return index


# tokenizer
def tokenization(file):
    tokenized = []
    lines = file.readlines()
    for line in lines:
        if line.startswith("<title>"):
            test = line[8:].strip()
            tokenizer = StandardTokenizer()
            tokenizer.setReader(StringReader(test))
            char = tokenizer.getAttribute(CharTermAttribute.class_)
            tokenizer.reset()
            tokens = []
            while tokenizer.incrementToken():
                tokens.append(char.toString())
            tokenized.append(tokens)
    return tokenized


def main():
    file = open('query.ohsu.1-63', 'r')
    step_one = tokenization(file)
    print(step_one)
    step_two = indextionization(step_one)
    print(step_two)


if __name__ == "__main__":
    main()











# StandardAnalyzer example.
# analyzer = StandardAnalyzer()
# stream = analyzer.tokenStream("", StringReader(test))
# stream.reset()
# tokens = []
# while stream.incrementToken():
#     tokens.append(stream.getAttribute(CharTermAttribute.class_).toString())
# print(tokens)
