from flask import Flask, request, make_response, jsonify, abort, Blueprint, current_app
import jwt
import datetime
from functools import wraps
import json, requests

api = Blueprint('APIs', __name__)
users = []
id = 0

def email_or_id_exist(id):
    
    global users
    
    try:
        current_app.logger.info("Looking for id %s in records" % (id))
        user_exist = [ user for user in users if user["email"] == id or user["id"] == id ]
        if user_exist:
            current_app.logger.info("%s found in records" % (id))
            return True
        else:
            current_app.logger.info("%s not found in records" % (id))
            return False
    except Exception as e:
        msg = "'%s' occured while finding for %s in records" % (str(e), id)
        current_app.logger.error(msg)
        return jsonify({"message" : msg }), 500
        
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("token")
        current_app.logger.info("Token : %s" % token)
        if not token:
            current_app.logger.error("Missing token in headers")
            return jsonify({"message": "Missing token in headers"}), 403
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"])
            current_app.logger.info("Data after decode: %s" % json.dumps(data))
        except:
            current_app.logger.error("Invalid Token %s" % (token))
            return jsonify({"message": "Invalid Token found in headers"}), 403
        return f(*args, **kwargs)
    return decorated

@api.route("/patch", methods=["PATCH"])
@token_required
def patch():
    try:
        json_object = request.json["json"]
        if not json_object:
            current_app.logger.error("JSON object is missing in the payload")
            return jsonify({"message": "Key Error: json key is missing"}), 500

        patch = request.json["patch"]
        if not patch:
            current_app.logger.error("JSON patch object is missing in the payload")
            return jsonify({"message": "Key Error: patch key is missing"}), 403
        res = jsonpatch.apply_patch(json_object, patch)
        return res
    except Exception as e:
        msg = "Exception %s occured while makig patch request" % str(e)
        current_app.logger.error(msg)
        return jsonify({"message": msg}), 500
    
@api.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        try:
            auth = request.authorization
            if auth is None:
                msg = "Unauthorized, Please enter Username and Password to login"
                current_app.logger.error(msg)
                abort(make_response(jsonify(message=msg), 401))

            if auth.username is '' or auth.password is '':
                message = "Unauthorized, either username or password is missing/empty"
                current_app.logger.error(message)
                return jsonify(message=message), 401

            token = jwt.encode( {
                'username': auth.username,
                'password': auth.password,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }, current_app.secret_key)
            current_app.logger.info("successfully authenticated")
            return jsonify({'token': token })
        except Exception as e:
            msg = "Exception %s found while login" % (str(e))
            current_app.logger.error(msg)
            return jsonify({'message': msg}), 500
            
@api.route("/users", methods=["POST", "GET"])
@token_required
def get_and_post_users():
    global users
    global id
    
    if request.method == "GET":
        msg = "Getting users list from records"
        current_app.logger.info(msg)
        return jsonify(users)
    
    elif request.method == "POST":
        try:
            new_user = request.get_json()
            if (not "email" in new_user) or (not "name" in new_user):
                msg = "Either email or name fields are missing in payload"
                current_app.logger.error(msg)
                return jsonify({"message": msg}), 500
            msg = "Adding user %s to the records" % (new_user)
            current_app.logger.info(msg)
            email = new_user["email"]
            if not email_or_id_exist(email):
                id = id + 1
                new_user["id"] = id
                users.append(new_user)
                msg = "successfully added user %s to the records" % (new_user)
                current_app.logger.info(msg)
                return jsonify(new_user)
            else:
                return jsonify("Email %s is already exist" % new_user["email"])
        except Exception as e:
            msg = "Exception %s found while adding user" % (str(e))
            current_app.logger.error(msg)
    else:
        abort(make_response(jsonify(message="Method not allowed"), 405))
           
@api.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
@token_required
def update_and_del_users(id):
    
    global users
    
    if request.method == "GET":
        if email_or_id_exist(id):
            user = [ user for user in users if user["id"] == id ]
            return jsonify(user)
        else:
            return "No user record found with id %s" % (id)
        
    elif request.method == "DELETE":

        if not email_or_id_exist(id):
            return "No user record found with id %s" % (id)        
        new_user_list = list(filter(lambda i: i['id'] != int(id), users))
        if len(users)-1 == len(new_user_list) :
            users = new_user_list
            return jsonify("Successfully deleted entry with id %s" % id) 
        
    elif request.method == "PUT":
        if not email_or_id_exist(id):
            return "No user record found with id %s" % (id)
        try:
            update_user = request.get_json()
            if not update_user:
                return jsonify(message="Missing fields"), 500
            for user in users:
                if user["id"] == id:
                    if "name" in user:
                        user["name"] = update_user["name"]
                    if "email" in user:
                        if not email_or_id_exist(update_user["email"]):
                            user["email"] = update_user["email"]
                        else:
                            return jsonify("Email %s is already exist" % update_user["email"])                        
                    return jsonify(user)
        except Exception as e:
            msg = "Exception %s found while updating user" % (str(e))
            current_app.logger.error(msg)            
    else:
        abort(make_response(jsonify(message="Method not allowed"), 405))

@api.route("/")
def root():
    return "Welcome to the page..!! please login at /login with anonymous username and password"

@api.route("/liveness")
def liveness():
    return "liveness, ok"

@api.route("/readiness")
def readiness():
    return "readiness, ok"
