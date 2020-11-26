import json

with open('./datasets/quac/train_v0.2.json') as quacFile:
  quacQuestions = json.load(quacFile)


questions=quacQuestions['data'][0]['paragraphs'][0]['qas'][1];