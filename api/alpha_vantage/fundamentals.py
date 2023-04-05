import os
import requests

ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'
KEY = os.environ.get('ALPHA_VANTAGE_KEY')

def get_balance_sheet(symbol: str):
    params = {
        'function': 'BALANCE_SHEET',
        'symbol': symbol,
        'apikey': KEY
    }

    response = requests.get(ALPHA_VANTAGE_URL, params=params)

    # TODO: Handle errors
    # TODO: Handle user selected period
    return response.json()['annualReports'][0]
