"""
Tools Modules Tests

Creator: Th3 0bservator > Security Researcher, Machine Learning Specialist
GitHub: https://github.com/guibacellar/th3ctf
Blog: https://www.theobservator.net/
"""

import unittest
from multi_tap_decoder_module import MultiTapDecoder


class MultiTapDecoderTest(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(
            MultiTapDecoder.decode_message('84433 02277773377788828666777 ;)'),
            'THE 0BSERVATOR ;)'
        )

if __name__ == '__main__':
    unittest.main()