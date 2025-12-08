from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
API_KEY = ''#insert api key here
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"


@app.get("/", response_class=HTMLResponse)
def weather_page(request: Request):
    return templates.TemplateResponse("weather.html", {"request": request, "data": None} )

@app.post("/", response_class=HTMLResponse)
def get_weather(request: Request, city: str = Form(...)):
    params = {'q':city, "appid":API_KEY, "units":"metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return templates.TemplateResponse('weather.html', {
        "request":request,
        "city":city,
        "data": data

    })
