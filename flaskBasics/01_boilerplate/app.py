from flask import Flask

app = Flask(__name__)

@app.route ('/')
def basic ():
    return '<h3>Hello World</h3>'

if __name__ == '__main__':
    app.run (debug=True)