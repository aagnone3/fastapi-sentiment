from fastapi import FastAPI

from fastapi_sentiment import sentiment_analysis
from fastapi_sentiment.models import (
    SentimentDocument,
    SentimentScoring,
    Message
)

app = FastAPI()


@app.get("/", response_model=Message, status_code=200)
def read_root() -> Message:
    return {
        'message': 'Hello World'
    }


@app.get("/health", response_model=Message, status_code=200)
async def get_health() -> Message:
    return {
        'message': 'Still kicking'
    }


@app.post("/sentiment", response_model=SentimentScoring, status_code=200)
async def get_sentiment(document: SentimentDocument) -> SentimentScoring:
    return sentiment_analysis.get_sentiment(document.text)
