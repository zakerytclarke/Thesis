import parser
import squad
import sys

#https://stackoverflow.com/questions/36610179/how-to-get-the-dependency-tree-with-spacy
#https://www.nltk.org/

# doc=parser.nlp("When did Beyonce start becoming popular?")
# for sentence in doc.sents:
#   print(sentence.root)


##Parse Tree
#print(parser.svo_parseTree("When did Beyonce start becoming popular?"))

##Parse Tree Visualized


def run():
  for q in range(442):
    print(q);
    resource=squad.getResource(q,0);
    for question in resource: 
      if(len(question["answers"])>0):
        print(question["question"]+"    "+question["answers"][0]["text"])
        print(parser.svo_parser(question["question"],question["answers"]))

def sample():
  file=open('./output/sample.txt','w');
  sys.stdout = file;
  for q in range(442):
    print("<PASSAGE>");
    print(squad.getArticle(q,0));
    print("</PASSAGE>");
    print("<ANSWER>");
    resource=squad.getResource(q,0);
    for question in resource: 
      if(len(question["answers"])>0):
        print(parser.svo_parser(question["question"],question["answers"])[0])
    print("</ANSWER>");

def sampleSummarizer():
  file=open('./output/sampleSummarizer.txt','w');
  sys.stdout = file;
  for q in range(442):
    article=squad.getArticle(q,0)
    summary=""
    resource=squad.getResource(q,0);
    for question in resource: 
      if(len(question["answers"])>0):
        print(parser.svo_parser(question["question"],question["answers"])[0])



def sampleSubjects():
  file=open('./output/sampleSubj.txt','w');
  sys.stdout = file;
  for q in range(442):
    print("<PASSAGE>");
    print(squad.getArticle(q,0));
    print("</PASSAGE>");
    print("<ANSWER>");
    resource=squad.getResource(q,0);
    for question in resource: 
      if(len(question["answers"])>0):
        temp2=parser.svo_parser(question["question"],question["answers"])[0][0]
        print(temp2[0]+" "+temp2[1]+" "+temp2[2])
    print("</ANSWER>");
    
