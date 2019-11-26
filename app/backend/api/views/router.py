# api/views/router.py
from flask import Blueprint, request, make_response, jsonify
from api.service import 
import json

# ルーティング設定
user_router = Blueprint('user_router', __name__)

@user_router.route('/user', methods=['GET'])
def getUserList():
  return make_response(jsonify({
    #json contents here
    "1": {
      "name": "hoge",
      "password": "gnuisnotunix"
    },
    "2": {
      "name": "fuga",
      "password": "phphypertextpreprocessor"
    }

  }))


@user_router.route('/users', methods=['POST'])
def registUser():
  pass