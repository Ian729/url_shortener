from flask import Flask, redirect, request
from flask_cors import CORS
import hashlib, json

app = Flask(__name__)
CORS(app)
url_mapping = {}

def generate_short_link(url):
    # 使用MD5哈希函数生成短链接
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]

@app.route('/shorten', methods=['POST'])
def shorten_url():
    print(request.data.decode('utf8'))
    form = json.loads(request.data.decode('utf8'))
    long_url = form.get('url')
    print("SERVER:", long_url)
    short_url = generate_short_link(long_url)
    url_mapping[short_url] = long_url
    return short_url

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        return redirect(url_mapping[short_url])
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
