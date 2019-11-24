from flask import Flask, request, make_response, jsonify, abort, Blueprint, current_app
import jwt
import datetime
from functools import wraps
import json, requests

api = Blueprint('APIs', __name__)
users = []
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        current_app.logger.info('Token : %s' %token)
        if not token:
            current_app.logger.error('Missing token' )
            return jsonify({'message': 'Missing token'}), 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_app.logger.info('Data after decode: %s' % json.dumps(data))
        except:
            current_app.logger.error('Invalid Token')
            return jsonify({'message': 'Invalid Token'}), 403
        return f(*args, **kwargs)
    return decorated

@api.route('/patch', methods=['PATCH'])
@token_required
def patch():
    json_object = request.json['json']
    if not json_object:
        current_app.logger.error('JSON object is missing in the payload')
        return jsonify({'message': 'Key Error: json key is missing'}), 500

    patch = request.json['patch']
    if not patch:
        current_app.logger.error('JSON patch object is missing in the payload' )
        return jsonify({'message': 'Key Error: patch key is missing'}), 403
    res = jsonpatch.apply_patch(json_object, patch)
    return res

@api.route('/login', methods=["POST"])
def login():

    if request.method == "POST":
        auth = request.authorization
        if auth is None:
            current_app.logger.error('Unauthorized, Please enter Username and Password to login')
            abort(make_response(jsonify(message="Unauthorized, please provide username and password"), 401))
        
        if auth.username is '' or auth.password is '':
            message = "Unauthorized, either username or password is missing/empty"
            current_app.logger.error(message)
            abort(make_response(jsonify(message=message), 401))

        token = jwt.encode( {
            'username': auth.username,
            'password': auth.password,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, current_app.secret_key)
        current_app.logger.info("successfully authenticated")
        return jsonify({'token': token })
    
@api.route('/users', methods=["POST", "GET"])
@token_required
def get_and_post_users():
    if request.method == "GET":
        return jsonify(users)
    elif request.method == "POST":
        user = request.get_json()
        users.append(user)
        return jsonify(users)
    else:
        abort(make_response(jsonify(message="Method not allowed"), 405))
           
@api.route('/users/<id>', methods=["GET", "PUT", "DELETE"])
@token_required
def update_and_del_users(id):
    global users
    if request.method == "GET":
        user = [ user for user in users if user["id"] == int(id) ]
        if user:
            return jsonify(user)
        else:
            return "No user record found with id %s" % (id)
        
    elif request.method == "DELETE":
        users = list(filter(lambda i: i['id'] != int(id), users))
        return jsonify(users)
    
    elif request.method == "PUT":
        update_user = request.get_json()
        print(update_user)
        for user in users:
            if user["id"] == int(id):
                user["name"] = update_user["name"]
                return jsonify(user)
    else:
        abort(make_response(jsonify(message="Method not allowed"), 405))
@api.route('/')
def root():
    return "Welcome to the page..!!"

@api.route('/liveness')
def liveness():
    return "liveness, ok"

@api.route('/readiness')
def readiness():
    return "readiness, ok"
