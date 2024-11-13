"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def x():
    member = request.json
    jackson_family.add_member(member)
    
    members = jackson_family.get_all_members()
   
    return jsonify(members), 200
    
@app.route('/members/<int:member_id>', methods=['GET'])
def y(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return "Member ID not found", 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def z(member_id):
    member = jackson_family.delete_member(member_id)
    if member == None:
        return 400, "member ID does not exist"
    elif jackson_family.get_member(member_id):
        return 500, "member not deleted"
    else: 
        return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PATCH'])
def a(member_id):
    change_data = request.get_json()
    member = jackson_family.patch_member(member_id, change_data)
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def b(member_id):
    change_data = request.get_json()
    member = jackson_family.put_member(member_id, change_data)
    return jsonify(member), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
