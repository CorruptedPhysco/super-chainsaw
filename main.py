from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
async def get_link():
    url = "https://bingotingo.com/best-social-media-platforms/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, "html.parser")
        link_element = soup.find('a', class_='su-button su-button-style-soft su-button-wide')
        
        if link_element and link_element.has_attr('href'):
            return {"link": link_element['href']}
        else:
            raise HTTPException(status_code=404, detail="Link element not found or missing href attribute")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request failed: {e}")

# To run the server, use the following command:
# uvicorn script_name:app --reload
