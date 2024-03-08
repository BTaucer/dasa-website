from fastapi import FastAPI, status, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', status_code=status.HTTP_200_OK)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get('/privatni-treninzi', status_code=status.HTTP_200_OK)
async def home(request: Request):
    return templates.TemplateResponse("privatni.html", {"request": request})


@app.get('/online-coaching', status_code=status.HTTP_200_OK)
async def home(request: Request):
    return templates.TemplateResponse("online.html", {"request": request})


@app.get('/jednokratni-planovi', status_code=status.HTTP_200_OK)
async def home(request: Request):
    return templates.TemplateResponse("jednokratni.html", {"request": request})


@app.get('/law', status_code=status.HTTP_200_OK)
async def law(request: Request):
    return templates.TemplateResponse("law_template.html", {"request": request})
