@echo off
start cmd /k "ollama run Almawave/Velvet:2B"
start cmd /k "uvicorn ollama_proxy:app --port 8000 --reload"
start cmd /k "python -m http.server 8080"
start "" http://localhost:8080