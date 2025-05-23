from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/api/velvet")
async def completions(request: Request):
    data = await request.json()
    prompt = data["messages"][-1]["content"]
    temperature = data.get("temperature", 0.4)

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "Almawave/Velvet:2B",
        "prompt": prompt,
        "stream": False,
        "temperature": temperature
    })

    if res.status_code != 200:
        return {"error": "Errore da Ollama", "detail": res.text}

    risposta = res.json()
    return {
        "choices": [{
            "message": {
                "content": risposta["response"]
            }
        }]
    }
