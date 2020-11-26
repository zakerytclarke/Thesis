import parser
import squad


doc=parser.nlp("When did Beyonce start becoming popular?")
for sentence in doc.sents:
  print(sentence)

#for question in squad.questions:
#  print(question["question"])
#  print(parser.svo_parser(question["question"],question["answers"]))

