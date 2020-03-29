from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Trail(Base):
    __tablename__ = 'trail'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    neighborhood = Column(String(200))
    distance = Column(Integer)
    status = Column(Boolean)

    def __init__(self, name, neighborhood, distance, status):
        self.name = name
        self.neighborhood = neighborhood
        self.distance = distance
        self.status = status

class TrailSchema(SQLAlchemySchema):
    class Meta:
        model = Trail
        load_instance = True

    id = auto_field()
    name = auto_field()
    neighborhood = auto_field()
    distance = auto_field()
    status = auto_field()
    
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

    db_session.add(new_trail)
    db_session.commit()

    return 'd' 

@app.route('/api/trail', methods=['GET']) # route is the endpoint
def get_trails():
    all_trails = db_session.execute("SELECT * FROM trail").fetchall()
    result = trails_schema.dump(all_trails)
    return jsonify(result) 


@app.route('/api/trail/<id>', methods=['DELETE']) # route is the endpoint
def delete_trail(id):
    db_session.query(Trail).filter(Trail.id == id).delete()
    db_session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
