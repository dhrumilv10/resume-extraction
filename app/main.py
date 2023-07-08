from flask import Flask

# app = Flask(__name__)


class HelloWorld:
    def __init__(self):
        self.hello = "Hello World"

    # @app.route("/")
    def hello_world(self):
        return self.hello


if __name__ == "__main__":
    # app.run(host="localhost", port=8000)
    obj = HelloWorld()
    print(obj.hello_world())
