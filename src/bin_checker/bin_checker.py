__all__ = ['get_bin']

import json
import os
from http import HTTPStatus

import requests


def get_bin(bin_number, timeout=5):
    """
    default timeout is set to 5 seconds by default
    """

    promptapi_endpoint = f'https://api.promptapi.com/bincheck/{bin_number}'
    apikey = os.environ.get('PROMPTAPI_TOKEN', None)
    if not apikey:
        return dict(error='You need to set PROMPTAPI_TOKEN environment variable')

    result = dict()
    headers = dict(apikey=apikey)
    http_error = None

    try:
        response = requests.request(
            'GET', promptapi_endpoint, timeout=timeout, headers=headers
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return dict(error='Connection timeout error')
    except requests.exceptions.TooManyRedirects:
        return dict(error='Too many redirects error')
    except requests.exceptions.ConnectionError:
        return dict(error='Connection error')
    except requests.exceptions.HTTPError as err:
        http_error = str(err)
    try:
        result = response.json()
    except json.decoder.JSONDecodeError as err:
        return dict(error=f'JSON decoding error: {str(err)}')

    if http_error:
        return dict(error=result.get('message', http_error))

    if response.status_code != HTTPStatus.OK.value:
        return dict(
            error=result.get('message', response.reason), status=response.status_code
        )
    return result
