from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    neighborhood = db.Column(db.String(200))
    distance = db.Column(db.Integer)
    status = db.Column(db.Boolean)

    def __init__(self, name, neighborhood, distance, status):
        self.name = name
        self.neighborhood = neighborhood
        self.distance = distance
        self.status = status

class TrailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'neighborhood', 'distance', 'status')

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/trail', methods=['POST'])
def post_trail():
    name = request.json['name']
    neighborhood = request.json['neighborhood']
    distance = request.json['distance']
    status = request.json['status']

    new_trail = Trail(name, neighborhood, distance, status)

    db.session.add(new_trail)
    db.session.commit()

    return trail_schema.jsonify(new_trail)

@app.route('/api/trail', methods=['GET']) # route is the endpoint
def get_trails():
    all_trails = Trail.query.all()
    result = trails_schema.dump(all_trails)
    return jsonify(result) 

if __name__ == '__main__':
    app.run(debug=True)
