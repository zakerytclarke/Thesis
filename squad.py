import json

with open('./datasets/squad/train-v2.0.json') as squadFile:
  squadQuestions = json.load(squadFile)

with open('./datasets/squad/dev-v2.0.json') as squadFile2:
  squadTest = json.load(squadFile2)

def getResource(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticle(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]["context"];

def articleCount():
  return len(squadQuestions['data']);

def getResourceTest(topic,paragraph):
  print(topic)
  return squadTest['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticleTest(topic,paragraph):
  return squadTest['data'][topic]['paragraphs'][paragraph]["context"];

def articleCountTest():
  return len(squadTest['data']);
