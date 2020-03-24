from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get_trails', methods=['GET']) # route is the endpoint
def get_trails():
    trails = [
                {
                'name': 'tryon creek',
                'distance': '2 miles',
                'neighborhood': 'lake oswego',
                'status': 'none',
                },
                { 
                'name': 'forest park',
                'distance': '5 miles',
                'neighborhood': 'downtown',
                'status': 'cool'
                },
                {
                'name': 'potato park',
                'distance': '5 miles',
                'neighborhood': 'france',
                'status': 'cool'
                },
            ]
    response = jsonify(trails)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

if __name__ == '__main__':
    app.run(debug=True)
