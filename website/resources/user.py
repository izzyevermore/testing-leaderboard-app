from flask_restful import Resource, reqparse
from website.models import User


class UserRegister(Resource):
    """
    This resource allows users to register by sedning a
    POST request with their id, email, password, firstname, notes,
    team_id, team_leader, work, points
    """
    parser = reqparse.RequestParser()
    parser.add_argument('')
