from flask import Flask

from modules.account.account import account_api

app = Flask(__name__)

app.register_blueprint(account_api)

@app.route("/")
def welcome():
    return "Welcome to the Python Server to use Temenos!"

if __name__ == "__main__":
    port = 8080
    app.run(port = port)