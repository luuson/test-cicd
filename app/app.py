from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_crypto():

    url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    res = requests.get(url, params=params)

    return res.json()


@app.route("/")
def home():

    data = get_crypto()

    btc = data["bitcoin"]["usd"]
    eth = data["ethereum"]["usd"]

    return render_template("index.html", btc=btc, eth=eth)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)