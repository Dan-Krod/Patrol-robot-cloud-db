from ..service.user_service import UserService
from flask_jwt_extended import create_access_token, get_jwt
from flask import jsonify
from .blocklist import BLOCKLIST

class UserController:
    @staticmethod
    def register(data):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400

        if UserService.authenticate(username, password):
            return jsonify({"error": "User already exists"}), 409

        UserService.register(username, password)
        return jsonify({"message": "User created successfully"}), 201

    @staticmethod
    def login(data):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400

        user = UserService.authenticate(username, password)
        if user:
            access_token = create_access_token(identity=str(user.id))
            return jsonify({"access_token": access_token}), 200

        return jsonify({"error": "Incorrect username or password"}), 401

    @staticmethod
    def logout():
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return jsonify({"message": "Successfully logged out"}), 200
