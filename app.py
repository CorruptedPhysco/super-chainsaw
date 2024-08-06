import os
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_link():
    url = "https://corruptedphysco.github.io/Tele-available/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, "html.parser")
        link_element = soup.find('a', class_='su-button su-button-style-soft su-button-wide')

        if link_element and link_element.has_attr('href'):
            return link_element['href']
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

@app.route('/', methods=['GET'])
def home():
    link = get_link()
    if link:
        return jsonify({"link": link})
    else:
        return jsonify({"error": "Link not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
