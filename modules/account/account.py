from flask import Blueprint
from flask import jsonify
from flask import current_app as app

from modules.models.temenos import Temenos

import requests


account_api = Blueprint('account_api', __name__)

@account_api.route('/accounts', methods=['GET'])
def get_accounts():
    r = Temenos().get_accounts()

    items = r.json()['_embedded']['item']
    data = []

    for account in items:
        simple_account = { 
            'id': account['AccountNumber'],
            'customer_id': account['Customer'],
            'currency': account['Currency']
        }

        data.append( simple_account )

    return jsonify(data)

@account_api.route('/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    r = Temenos().get_account(account_id)
    account = r.json()
    account_details = {
        'id': account['Acc'],
        'account_name': account['Ac1'],
        'customer_id': account['Customer'],
        'balance': account['RealBalance'],
        'bank': account['Branch']
    }

    return jsonify(account_details)
