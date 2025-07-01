from flask import Flask, request, jsonify
from datastructures import FamilyStructure

app = Flask(__name__)

# Creamos la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Obtener todos los miembros
@app.route("/members", methods=["GET"])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Obtener un solo miembro por ID
@app.route("/members/<int:id>", methods=["GET"])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if member is not None:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Agregar un nuevo miembro
@app.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()
    member = jackson_family.add_member(data)
    return jsonify(member), 200

# Eliminar un miembro
@app.route("/members/<int:id>", methods=["DELETE"])
def delete_member(id):
    deleted = jackson_family.delete_member(id)
    if deleted:
        return jsonify({"done": True, "id": deleted["id"]}), 200
    else:
        return jsonify({"error": "Member not found"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)
