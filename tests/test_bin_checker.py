# pylint: disable=R0201,E1101

import os
import unittest
from collections import namedtuple

from console import console

from bin_checker import get_bin

console = console(source=__name__)

EXISTING_PROMPTAPI_TOKEN = os.environ.get('PROMPTAPI_TOKEN', None)


class TestSimple(unittest.TestCase):
    def test_api_token(self):
        os.environ['PROMPTAPI_TOKEN'] = ''  # noqa: S105

        bin_information = get_bin('302596')

        self.assertTrue(bin_information.get('error', False))
        self.assertEqual(
            'You need to set PROMPTAPI_TOKEN environment variable',
            bin_information.get('error', None),
        )

    def test_real_request(self):
        os.environ['PROMPTAPI_TOKEN'] = EXISTING_PROMPTAPI_TOKEN

        bin_information = get_bin('302596')
        if bin_information.get('error', False):
            result = namedtuple('result', bin_information.keys())(**bin_information)
            console('bin_information', bin_information)

            self.assertEqual(result.bank_name, 'Diners Club International')
            self.assertEqual(result.country, 'United States Of America')
            self.assertEqual(result.url, 'www.dinersclub.com')
            self.assertEqual(result.type, 'Credit')
            self.assertEqual(result.scheme, 'Discover')
            self.assertEqual(result.bin, '302596')


if __name__ == '__main__':
    unittest.main()
