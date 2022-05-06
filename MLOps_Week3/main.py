import uvicorn
from fastapi import FastAPI, HTTPException, status, Request, Form
from fastapi.templating import Jinja2Templates

from transformers import pipeline
from requests import Session
from pydantic import BaseModel

import logging
from logging.config import dictConfig
from MLOps_Week3.log_config import log_config # this is your local file

dictConfig(log_config)
logger = logging.getLogger("my_logger") # should be this name unless you change it in log_config.py

classifier = pipeline("sentiment-analysis",model='distilbert-base-uncased-finetuned-sst-2-english')
# classifier = pipeline("sentiment-analysis",model='MLOps_Week3/model')

app = FastAPI()


@app.get('/')
def hello_world():
    logger.info("at root")
    return {'message': 'Hello, World!'}



# Define the API endpoints
@app.get('/health' ,status_code=status.HTTP_200_OK)
def perform_healthcheck():
    logger.info("healthcheck endpoint")
    return {'healthcheck': 'Everything OK!'}

@app.get('/test')
def test():
    logger.info("test endpoint")
    return {'test':'test endpoint'}




class PredictionRequest(BaseModel):
  query: str

templates = Jinja2Templates(directory="MLOps_Week3/templates")

@app.get("/form")
def form_get(request: Request):
    logger.info('get form request')
    return templates.TemplateResponse('form.html', context={'request': request})

@app.post("/form")
def form_post (request: Request, comment: str = Form(...)):
    logger.info('post sentiment result')
    result = "This comment is " + classifier(comment)[0].get('label')
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/sentiment")
async def get_sentiment(request: PredictionRequest):
    result = "This comment is " + classifier(request.query)[0].get('label')
    return {'comment': request.query,"sentiment":result}
