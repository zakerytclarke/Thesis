import parser
import squad
import sys
import csv



def validate(filename):
  file=open('./validation/sample.txt','w');
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