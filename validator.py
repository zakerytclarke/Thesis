import parser
import squad
import sys
import csv
import svo




def validate(filename):
    dataset="test"
    with open('./validation/'+filename) as file:
        validationTxt=file.read()
        instances=validationTxt.split("\n")
        print("Generarting Graphs")
        instances=list(map(svo.generateGraph,instances))
        #Generate for annotated set
        annotated=[]
        for q in range(squad.articleCount(dataset)):
            for r in range(squad.paragraphCount(q,dataset)):
                article=squad.getArticle(q,r,dataset)
                resource=squad.getResource(q,r,dataset);
                qs=[]
                for question in resource:
                  if(len(question["answers"])>0):
                    temp=parser.svo_parser(question["question"],question["answers"])[0]
                    qs.append(temp)
                annotated.append(qs)
        print("Evaluating Metric")
        em=0
        f1=0
        count=0
        for i,graph in enumerate(instances): # For every generated instance
            count+=1
            f1+=svo.stats(graph,annotated[i])
            if svo.findMatchGraphs(graph,annotated[i]):
                em+=1
        print(em/count)
        print(f1/count)
