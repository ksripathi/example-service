from flask import Flask, request, make_response, jsonify, abort
from flask import send_file, Blueprint, current_app
import jwt
import datetime
from functools import wraps
import json, requests

api = Blueprint('APIs', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        current_app.logger.info('Token : %s' %token)
        if not token:
            current_app.logger.error('Missing token' )
            return jsonify({'message': 'Missing tokne'}), 403
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

@api.route('/login')
def login():
    auth = request.authorization
    if auth and auth.username and auth.password:
        current_app.logger.info('authentication sucessful')
        token = jwt.encode({'user':auth.username, 'exp': \
                            datetime.datetime.utcnow() + \
                            datetime.timedelta(minutes=30)}, current_app.secret_key)
        return jsonify({'token':token})
    current_app.logger.error('Unauthorized. Please enter Username and Password to login')
    return make_response('Un Authorized', 401, {'WWW-Authenticate':'Basic-realm="Login required!"'})
