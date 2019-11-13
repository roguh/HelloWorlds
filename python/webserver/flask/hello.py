from flask import Flask, request

app = Flask(__name__)
template = '''<html>
    <head>
        <title>HELLO-WORLD SERVER</title>
    </head>
    <body>
        <h1>Hello</h1>
        <p>{}!</p>
    </body>
    </html>
'''


@app.route("/")
def main():
    return template.format('world')


@app.route("/to-recipient", methods=["POST"])
def custom():
    return template.format(request.json['recipient'])


if __name__ == "__main__":
    app.run()
