import parser
import squad

#https://stackoverflow.com/questions/36610179/how-to-get-the-dependency-tree-with-spacy
#https://www.nltk.org/

# doc=parser.nlp("When did Beyonce start becoming popular?")
# for sentence in doc.sents:
#   print(sentence.root)


##Parse Tree
#print(parser.svo_parseTree("When did Beyonce start becoming popular?"))

##Parse Tree Visualized


def run():
  for question in squad.questions:
    print(question["question"]+"    "+question["answers"][0]["text"])
    print(parser.svo_parser(question["question"],question["answers"]))
 