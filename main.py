import json

# запрос на страница сайта с ответом
import requests

from flask import Flask

# print(text)


app = Flask(__name__)


@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    result = ''
    for currency in currencies['Valute']:
        result += str(currency) + '<br>'

    result=text+result
    return result


if __name__ == "__main__":
    app.run()
