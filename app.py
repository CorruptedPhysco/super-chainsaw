from fastapi import FastAPI
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/get-link")
async def get_link():
    url = "https://bingotingo.com/best-social-media-platforms/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    link_element = soup.find('a', class_='su-button su-button-s')

    if link_element and link_element.has_attr('href'):
        return JSONResponse(content={'link': link_element['href']})
    return JSONResponse(content={'link': None})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
