from flask import render_template, jsonify, make_response, request
from models import Professor, User, Comment
from database import Session
from sonata import app


session = Session()

@app.route('/clients/departments', methods=['GET'])
def departments():
    departments = [dept.department for dept in session.query(Professor.department).distinct()]
    return jsonify({"departments":departments})

'''
@app.rout('/clients/comments', methods['POST'])
def post_comment():
    if not request.json or not 'comment' in request.json:
        abort(400)
    session.add(Comment(user=request.json['user'], comment=request.json['comment'], date=request.json['date'], professor=request.json['professor']))
    session.commit()
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"Not found"}), 404)



@app.route('/clients/professors/<string:department>', methods['GET'])




@app.route('/clients/login', methods=['POST'])
'''
