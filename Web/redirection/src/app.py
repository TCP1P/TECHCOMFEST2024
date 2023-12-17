from flask import Flask, request
import requests
import re
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "fake{flag}")

@app.get("/")
def home():
    url = request.args.get("url", False)
    if not url:
        return "Url not found"
    if not re.match(r"^https://youtube.com/.*$", url):
        return "url isn't youtube url"
    response = requests.get(url+"?"+FLAG)
    return response.text


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=False)
