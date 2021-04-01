from flask import jsonify, request
from app import app, db
from app.models import User
from app.schemas import users_schema, user_schema

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

# @app.route('/create_user')
# def create_user():
#     username = request.json['username']
#     email = request.json['email']
#     password = request.json['password']
#     if User.query.filter_by(username=username).first() is None:
#         new_user = User(username=username, email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify(user_schema.dump(new_user))
#     return jsonify({"message": "username taken"})
    

# @app.route('/create_user')
# def create_user():
#     username = request.json['username']
#     email = request.json['email']
#     password = request.json['password']
#     try:
#         new_user = User(username=username, email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#     except:
#         return jsonify({"message": "username taken"})
#     else:
#         return jsonify(user_schema.dump(new_user))

@app.route('/create_user')
def create_user():
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
    except:
        return jsonify({"message": "username taken"})
    try:
        new_user = User(username=username, email=email, password=password)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({"message": "username taken"})
    else:
        return jsonify(user_schema.dump(new_user))