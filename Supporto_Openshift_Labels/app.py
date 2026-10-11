import os

from flask import Flask

app = Flask(__name__)


APP_NAME = os.getenv("APP_NAME", "openshift-web-lab")
APP_ENV = os.getenv("APP_ENV", "dev")
APP_REGION = os.getenv("APP_REGION", "EU")


@app.route("/")
def home():
    return f"""
    <h1>{APP_NAME}</h1>
    <p>Ambiente: {APP_ENV}</p>
    <p>Regione: {APP_REGION} </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
