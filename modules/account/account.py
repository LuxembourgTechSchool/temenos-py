from flask import Blueprint
from flask import jsonify

account_api = Blueprint('account_api', __name__)

@account_api.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify([])
