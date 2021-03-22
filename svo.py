import parser
import squad


def generateGraph(txt):
    statements=txt.split(".")
    statements=list(map(parser.svo,statements))
    return statements


def equal(s1,s2):
    return s1[0].lower()==s2[0].lower() and s1[1].lower()==s2[1].lower() and s1[2].lower()==s2[2].lower()

def match(s1,s2):
    return (s1[0].lower()==s2[0].lower() or s1[2].lower()==s2[2].lower()) or s1[2].lower()==s2[2].lower()

def inGraph(svo,graph):
    for inst in graph:
        if equal(inst,svo):
            return True
    return False

def findMatch(svo,graph):
    for inst in graph:
        if match(inst,svo):
            return inst
    return None


def inGraphs(g1,g2):
    for inst in g1:
        if inGraph(inst,g2):
            return True
    return False

def findMatchGraphs(g1,g2):
    for inst in g1:
        if findMatch(inst,g2):
            return True
    return False

def graphToString(g):
    def fgg(ggg):
        return ggg+" "
    def fg(gg):
        return list(map(fgg,gg))

        return gg+" "
    return "".join(sum(list(map(fg,g)),[]))+ " "

def graphToAnswerString(g):
    return " ".join(list(map(lambda x: x[2]+" ",g)))

def countSameDifference(t1,t2):
    txt1=t1.split(" ")
    txt2=t2.split(" ")
    tp=0
    for tt1 in txt1:
        #bool=False
        for tt2 in txt2:
            if(tt1==tt2): #and bool=False:#Item in ls 1 is in ls 2 and hasnt been marked
                #bool=True
                tp+=1
    fp=len(txt1)-tp
    fn=len(txt2)-tp
    return [tp,fp,fn]



def stats(g1,g2):
    [tp,fp,fn]=countSameDifference(graphToString(g1),graphToString(g2))
    precision=0.75*tp/(tp+fp)
    recall=tp/(tp+fn)
    f1=(precision*recall)/(precision+recall)
    # print(precision,recall)
    return f1
