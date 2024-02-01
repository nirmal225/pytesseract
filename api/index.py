from flask import Flask, request
from flask_cors import CORS
from Pytesseract import Pytesseract

app = Flask(__name__)
CORS(app)


@app.route("/captcha")
def hello_world():
    encoded_text = request.args.get('encodedData').replace(" ", "+")
    py = Pytesseract()
    py.save_mage(encoded_text)
    return {'captcha': py.get_captcha().replace("", "")}


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
