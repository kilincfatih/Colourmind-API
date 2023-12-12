# renk paleti şablonlarının veya temalarının isimlerinin bulunduğu API

import requests
import json
from flask import Flask

# app adında bşr flask sınıfı oluşturur
app = Flask(__name__)

@app.route('/')
def index():

# "http://colormind.io/list/" URL bilgisine göre API renk listesini url değişkenine atar
    url = "http://colormind.io/list/"

# Belirtilen URL'den get isteği yapar ve response değişkenine atar
    response = requests.get(url)

# response değişkeninin yanıtını JSON formatında alır data değişkenine atar
    data = response.json()

# Okunabilirliği arttırmakiçin 4 boşlukluk girinti yapar ve metin gibi gösterilmesini sağlar
    formatted_data = json.dumps(data, indent=4)
    return '<pre>' + formatted_data + '</pre>'

# Flask uygulamasını 6767 port üzerinde çalıştırır
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6767)
