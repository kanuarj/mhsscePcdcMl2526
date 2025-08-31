from flask import Flask

app = Flask(__name__)

@app.route ('/mhssce')
def basic ():
    return '<h3>Hello World</h3>'

@app.route('/')
def saysHello():
    return 'Hello from Mumbai'

@app.route('/mhssce/<name>')
def greets (name):
    return f'Hello to {name} by MHSSCE'

if __name__ == '__main__':
    app.run (debug=True)