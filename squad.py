import json

with open('./datasets/squad/train-v2.0.json') as squadFile:
  squadQuestions = json.load(squadFile)

with open('./datasets/squad/dev-v2.0.json') as squadFile:
  squadTest = json.load(squadFile)

def getResource(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticle(topic,paragraph):
  return squadQuestions['data'][topic]['paragraphs'][paragraph]["context"];


def getResourceTest(topic,paragraph):
  return squadTest['data'][topic]['paragraphs'][paragraph]['qas'];

def getArticleTest(topic,paragraph):
  return squadTest['data'][topic]['paragraphs'][paragraph]["context"];
