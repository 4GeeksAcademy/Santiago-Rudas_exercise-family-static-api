from flask import Flask, request, jsonify, url_for
from datastructures import FamilyStructure

app = Flask(__name__)

# Creamos la familia Jackson
jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 400

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Missing required member data"}), 400

    jackson_family.add_member(data)
    return jsonify({"message": "Member added successfully"}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 400

    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

# Ejecutar servidor solo si es el archivo principal
if __name__ == '__main__':
    app.run(debug=True)
