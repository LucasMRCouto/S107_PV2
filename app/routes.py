from flask import jsonify, request
from app.services import create_user, get_user, get_all_users, update_user, delete_user

def configure_routes(app):
    @app.route("/users", methods=["GET"])
    def list_users():
        users = [user.to_dict() for user in get_all_users()]
        return jsonify(users), 200

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_single_user(user_id):
        user = get_user(user_id)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        return jsonify(user.to_dict()), 200

    @app.route("/users", methods=["POST"])
    def create_user_route():
        data = request.json
        try:
            user = create_user(data["id"], data["username"], data["password"], data["name"])
            return jsonify(user.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/users/<int:user_id>", methods=["PUT"])
    def update_user_route(user_id):
        data = request.json
        try:
            user = update_user(user_id, data["username"], data["password"], data["name"])
            return jsonify(user.to_dict()), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @app.route("/users/<int:user_id>", methods=["DELETE"])
    def delete_user_route(user_id):
        try:
            delete_user(user_id)
            return jsonify({"message": "Usuário deletado com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
