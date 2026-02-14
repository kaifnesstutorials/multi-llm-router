from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml
import json

from router import LLMRouter
from providers.groq_provider import GroqProvider
from providers.openai_provider import OpenAIProvider


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load config
with open("config/providers.yaml") as f:
    config = yaml.safe_load(f)

providers = []

for p in config["providers"]:
    if p["name"] == "groq":
        providers.append(GroqProvider(p))
    elif p["name"] == "openai":
        providers.append(OpenAIProvider(p))


router = LLMRouter(providers)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate(data: dict):

    prompt = data.get("prompt")

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt required")

    try:
        result = await router.route(prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
def get_stats():
    with open("logs/usage.json", "r") as f:
        data = json.load(f)
    return data
