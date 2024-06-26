import json

from flask import Blueprint

from api.api import api_root
from database.models import Candidate

user_root = Blueprint('user', __name__, url_prefix="{}/user".format(api_root.url_prefix))


@user_root.route('/', methods=['GET'])
@user_root.route('/<int:user_id>', methods=['GET'])
def get_user(user_id=""):
    if not user_id: # hackathon
        return json.dumps([c.serialize() for c in Candidate.query.all()])
    return Candidate.query.filter_by(user_id).first().serialize()
