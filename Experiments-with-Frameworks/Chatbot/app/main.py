from typing import Optional

from fastapi import FastAPI

import chatbot as cb

app = FastAPI()


@app.post("/send/{text}")
def send(text):
    return {"response": cb.chatbot_response(text)}


@app.get("/")
def read_root():
    return {"response": "Hello World!"}

