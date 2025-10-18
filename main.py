from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone

app = FastAPI()

CATFACT= "https://catfact.ninja/fact"

@app.get("/me", response_class=JSONResponse)
def get_profile():
    try:
        # Fetch cat fact from external API
        response = requests.get(CATFACT, timeout=5)
        response.raise_for_status()
        data = response.json()
        fact = data.get("fact", "Cats are mysterious creatures!")
    except requests.exceptions.RequestException:
        
        fact = "Please try again later."

    # response
    result = {
        "status": "success",
        "user": {
            "email": "preciousajorgba@gmail.com",
            "name": "Ajorgba Precious Eka",      
            "stack": "Python"      
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }

    return JSONResponse(content=result, media_type="application/json")
