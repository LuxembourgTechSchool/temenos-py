from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Python Server to use Temenos!"

if __name__ == "__main__":
    port = 8080
    app.run(port = port)