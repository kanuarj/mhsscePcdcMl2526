from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route ('/', methods = ['POST'])
@cross_origin()
def basic ():
    firstname = request.json['firstname']
    return jsonify({
        'output' : f'Hello {firstname}'
    })

if __name__ == '__main__':
    app.run (debug=True)