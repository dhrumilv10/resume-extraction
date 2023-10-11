import os
from flask import Flask

app = Flask(__name__)

# def

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("-------Starting app on PORT 5000----------")

    app.run(debug=True, port=port, host='0.0.0.0')
    print("Hello World")
