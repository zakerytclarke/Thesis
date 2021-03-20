import json

with open('./datasets/squad/train-v2.0.json') as squadFile:
  squadQuestions = json.load(squadFile)

with open('./datasets/squad/dev-v2.0.json') as squadFile2:
  squadTest = json.load(squadFile2)

def getResource(topic,paragraph,dataset):
  if dataset=="train":
    return squadQuestions['data'][topic]['paragraphs'][paragraph]['qas'];
  else:
    return squadTest['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticle(topic,paragraph,dataset):
  if dataset=="train":
    return squadQuestions['data'][topic]['paragraphs'][paragraph]["context"];
  else:
    return squadTest['data'][topic]['paragraphs'][paragraph]["context"];

def articleCount(dataset):
  if dataset=="train":
    return len(squadQuestions['data']);
  else:
    return len(squadTest['data']);
  


def paragraphCount(topic,dataset):
  if dataset=="train":
    return len(squadQuestions['data'][topic]['paragraphs'])
  else:
    return len(squadTest['data'][topic]['paragraphs'])
 