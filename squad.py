import json

with open('./datasets/squad/train-v2.0.json') as squadFile:
  squadQuestions = json.load(squadFile)

def getResource(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticle(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]["context"];
