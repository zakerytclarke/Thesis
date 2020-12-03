import spacy
from spacy import displacy
from spacy.matcher import Matcher  

nlp = spacy.load("en_core_web_sm")

spacy.explain("acomp")

## Parser to convert questions to Subject, Verb, Object triplets
# dependency markers for subjects
SUBJECTS = {"nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl", "subj"}
# dependency markers for objects
OBJECTS = {"dobj","acomp","iobj"}
# POS tags that will break adjoining items
BREAKER_POS = {"CCONJ", "VERB"}
# words that are negations
NEGATIONS = {"no", "not", "n't", "never", "none"}



def sov_triplets(text):
  parsed_text = nlp(text)
  subj=""
  verb=""
  obj=""
  for token in parsed_text:
    if (token.dep_=="nsubj") : subj=token.lemma_
    if (token.dep_=="xcomp") : verb=token.lemma_
    if token.dep_ in OBJECTS: obj=token.lemma_
    print(token,token.dep_,token.lemma_)
  return (subj,verb,obj)

def svo(text):
  
  parsed_text = nlp(text)

  subj=""
  verb="is"
  obj=""

  #Get noun phrases
  entitites=[ent.text for ent in parsed_text.ents]
  nouns=[chunk.text for chunk in parsed_text.noun_chunks]
  
  nouns=(sorted(nouns, key=lambda s: (-1,) if containsEntity(s,entitites) else (1,) ))
  nouns=(sorted(nouns, key=lambda s: (-1,) if s[0].isupper() else (1,) ))
  #Get verb phrases
  #pattern = [{'POS': 'VERB', 'OP': '?'},
  #           {'POS': 'ADV', 'OP': '*'},
  #          {'POS': 'VERB', 'OP': '+'}]
  # matcher = Matcher(nlp.vocab) 
  verbs=[token.lemma_ for token in parsed_text if token.pos_ == "VERB"]


  
  if (len(nouns)>0) : subj=nouns[0]
  if (len(verbs)>0) : verb=verbs[0]
  if (len(nouns)>1) : obj=nouns[1]
  return [subj,verb,obj]

def containsEntity(str,entitites):
  for ent in entitites:
    if ent in str:
      return True
  return False


def sov_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


def replaceAnswer(svo,answer):
  if(svo[0]==""):
    svo[0]=answer
  else:
    if(svo[1]==""):
      svo[1]=answer
    else:
      if(svo[2]==""):
        svo[2]=answer
      else: 
        svo[2]=answer
  return svo

def svo_parser(text,answers):
  svos=svo(text)
  if("what" in svos[0].lower()):
    svos[0]=svos[2]
    svos[2]=""
  if("who" in svos[2].lower()):
    svos[0]=svos[2]
    svos[2]=""

  #Insert blanks for question phrases
  if(("what" in svos[0].lower()) or
     ("who" in svos[0].lower()) or
     ("when" in svos[0].lower()) or
     ("where" in svos[0].lower()) or 
     ("why" in svos[0].lower()) or
     ("which" in svos[0].lower()) or
     ("how" in svos[0].lower())
     ):
    svos[0]=""
  if(("what" in svos[1].lower()) or
     ("who" in svos[1].lower()) or
     ("when" in svos[1].lower()) or
     ("where" in svos[1].lower()) or
     ("why" in svos[1].lower()) or
     ("which" in svos[1].lower()) or
     ("how" in svos[1].lower())
     ):
    svos[1]=""
  if(("what" in svos[2].lower()) or
     ("who" in svos[2].lower()) or
     ("when" in svos[2].lower()) or
     ("where" in svos[2].lower()) or
     ("why" in svos[2].lower()) or
     ("which" in svos[2].lower()) or
     ("how" in svos[2].lower())
     ):
    svos[2]=""
  out=[];
  for x in answers:
    temp=svos.copy()
    out.append(replaceAnswer(temp,x["text"]))
  return out


def svo_parseTree(text):
  parsed_text = nlp(text)

  for token in parsed_text:
    print(token.dep_)


def renderParseTree(text):
  parsed_text = nlp(text)
  displacy.serve(parsed_text,style="dep")