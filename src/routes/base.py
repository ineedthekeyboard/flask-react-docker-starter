"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

BASE_BLUEPRINT = Blueprint("base", __name__)

@BASE_BLUEPRINT.route('/<string:echo>')
def get_version(echo):
    return f"Hello World!!@# dsa{echo}"
