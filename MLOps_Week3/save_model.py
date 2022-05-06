from transformers import pipeline
import json

classifier = pipeline("sentiment-analysis",model='distilbert-base-uncased-finetuned-sst-2-english')
path='model'
classifier.save_pretrained(path)
