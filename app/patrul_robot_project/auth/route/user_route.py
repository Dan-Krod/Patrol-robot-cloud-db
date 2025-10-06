from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..controller.user_controller import UserController

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("/register", methods=["POST"])
def register():
    """
    User registration
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: newuser
            password:
              type: string
              example: mypassword
    responses:
      201:
        description: User created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: User created successfully
      400:
        description: Username or password missing
      409:
        description: User already exists
    """
    data = request.json
    return UserController.register(data)


@user_blueprint.route("/login", methods=["POST"])
def login():
    """
    User login
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: secret123
    responses:
      200:
        description: Successful login, JWT access token returned
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
      400:
        description: Missing username or password
      401:
        description: Incorrect username or password
    """
    data = request.json
    return UserController.login(data)


@user_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    User logout
    ---
    tags:
      - Authentication
    security:
      - BearerAuth: []
    consumes:
      - application/json
    responses:
      200:
        description: Successfully logged out
        schema:
          type: object
          properties:
            message:
              type: string
              example: Successfully logged out
    """
    return UserController.logout()


@user_blueprint.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    """
    Protected route example
    ---
    tags:
      - Authentication
    security:
      - BearerAuth: []
    responses:
      200:
        description: Access granted
        schema:
          type: object
          properties:
            message:
              type: string
              example: This is a protected route
      401:
        description: Missing or invalid token
    """
    return {"message": "This is a protected route"}, 200
