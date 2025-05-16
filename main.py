from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

class URLRequest(BaseModel):
    url: HttpUrl

@app.post("/validate-url/")
async def validate_url(request: URLRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(str(request.url))
            status_code = response.status_code
            if status_code != 200:
                raise HTTPException(status_code=400, detail="URL is not accessible.")
            
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No title found"
            
            return {
                "url": request.url,
                "status_code": status_code,
                "title": title
            }
    except httpx.RequestError:
        raise HTTPException(status_code=400, detail="Failed to fetch the URL.")

@app.get("/")
async def root():
    return {"message": "Welcome to the URL Validator API. Use the /validate-url/ endpoint to validate URLs."}
