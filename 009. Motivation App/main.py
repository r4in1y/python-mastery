from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
base_url = "https://zenquotes.io/api/random/"
templates = Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET", "POST"])
def get_quote(request: Request):
    response = requests.get(base_url)
    data = response.json()
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
