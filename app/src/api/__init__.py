from flask import Blueprint, jsonify, blueprints

api = Blueprint(name='api',)

@api.route('/get_test', methods=['GET'])
def get_test():
    return jsonify({
        "method": "GET request"
    })

@api.route('/post_test')
def post_test():
        return jsonify({
        "method": "POST request"
    })

@api.route('/put_test')
def put_test():
        return jsonify({
        "method": "PUT request"
    })

@api.route('/delete_test')
def delete_test():
        return jsonify({
        "method": "DELETE request"
    })
