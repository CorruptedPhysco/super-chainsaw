from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/get-link', methods=['GET'])
def get_link():
    url = "https://bingotingo.com/best-social-media-platforms/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    link_element = soup.find('a', class_='su-button su-button-s')

    if link_element and link_element.has_attr('href'):
        return jsonify({'link': link_element['href']})
    return jsonify({'link': None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
