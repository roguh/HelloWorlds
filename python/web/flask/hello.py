from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello, world!\n"


@app.route("/to-recipient", methods=["POST"])
def custom():
    return "Hello, {}!\n".format(request.json['recipient'])


if __name__ == "__main__":
    app.run()
