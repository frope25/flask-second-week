from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1 style="color:red; font-size:12rem;"> hello world </h1>'

if __name__ == "__main__":
    app.run(debug=True)