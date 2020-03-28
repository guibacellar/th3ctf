"""
Multi-tap Phone Decoder Module (REF> https://en.wikipedia.org/wiki/Multi-tap)

Creator: Th3 0bservator > Security Researcher, Machine Learning Specialist
GitHub: https://github.com/guibacellar/th3ctf
Blog: https://www.theobservator.net/
"""


class MultiTapDecoder:

    __MAP = {
        '1': '',
        '2': 'A', '22': 'B', '222': 'C',
        '3': 'D', '33': 'E', '333': 'F',
        '4': 'G', '44': 'H', '444': 'I',
        '5': 'J', '55': 'K', '555': 'L',
        '6': 'M', '66': 'N', '666': 'O',
        '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
        '8': 'T', '88': 'U', '888': 'V',
        '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z'
    }

    @staticmethod
    def decode_message(message):
        """
        Decode Input Multi-Tap Message

        :param message: Encoded Message
        :return: Decoded Message
        """

        # Split Message in Sub Components
        to_decode = []
        decode_buff = ''
        last_byte = ''

        for current_char in message:

            if last_byte != '' and last_byte != current_char:
                to_decode.append(decode_buff)
                decode_buff = ''

            decode_buff += current_char
            last_byte = current_char

        to_decode.append(decode_buff)

        result_message = ''.join([
            MultiTapDecoder.__MAP[item] if item in MultiTapDecoder.__MAP else item
            for item
            in to_decode
        ])

        return result_message
