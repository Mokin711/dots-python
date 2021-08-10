import base64
import requests

import dots
from dots import token


class Transaction():

    @classmethod
    def create(user_id, amount, reciept=None, breakdown=None, notes=None, allow_debit=False):

        json = {
            'user_id': user_id,
            'amount': amount,
            'reciept': reciept,
            'breakdown': breakdown,
            'notes': notes,
            'allow_debit': allow_debit
        }

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = requests.post(
            dots.api_base + '/transactions/create', json=json, headers=headers)
        data = response.json()

        if data['success']:
            return data['transaction']
        else:
            raise Exception(data['message'])

    @classmethod
    def get(transaction_id):

        headers = {
            'Authorization': 'Basic ' + token.get_auth_token()
        }

        response = requests.get(
            dots.api_base + '/transactions/get/transaction/' + transaction_id, headers=headers)
        data = response.json()

        if data['success']:
            return data['transaction']
        else:
            raise Exception(data['message'])
