from flask import Blueprint
from flask import jsonify
from flask import current_app as app

from modules.models.temenos import Temenos

import requests


account_api = Blueprint('account_api', __name__)

@account_api.route('/accounts', methods=['GET'])
def get_accounts():
    temenos = Temenos()
    r = temenos.get_accounts()
    return jsonify(r.json())

@account_api.route('/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    temenos = Temenos()
    r = temenos.get_account(account_id)
    return jsonify(r.json())
