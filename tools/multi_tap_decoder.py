"""
Multi-tap Phone Decoder (REF> https://en.wikipedia.org/wiki/Multi-tap)

Creator: Th3 0bservator > Security Researcher, Machine Learning Specialist
GitHub: https://github.com/guibacellar/th3ctf
Blog: https://www.theobservator.net/

*************** Usage ***************
> Direct Text Mode
python multi_tap_decoder.py "MESSAGE_HERE"

> Input File Mode
python multi_tap_decoder.py -f "myfile.ext"
"""

import sys
from modules import multi_tap_decoder_module

BANNER = '''
████████╗██╗  ██╗██████╗      ██████╗ ██████╗ ███████╗███████╗██████╗ ██╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗
╚══██╔══╝██║  ██║╚════██╗    ██╔═████╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ███████║ █████╔╝    ██║██╔██║██████╔╝███████╗█████╗  ██████╔╝██║   ██║███████║   ██║   ██║   ██║██████╔╝
   ██║   ██╔══██║ ╚═══██╗    ████╔╝██║██╔══██╗╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ██║  ██║██████╔╝    ╚██████╔╝██████╔╝███████║███████╗██║  ██║ ╚████╔╝ ██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
'''


def main(argv):
    print(BANNER)

    if len(argv) == 0:
        print('Use:')
        print('python multi_tap_decoder.py "MESSAGE_HERE"')
        print('or')
        print('python multi_tap_decoder.py -f "myfile.ext"')
        exit(0)

    content_to_decode = []
    if argv[0] == '-f':
        print("[*] File Mode Selected")

        # Check if File contains \
        if '\\' in argv[1]:
            print('[ERROR] Check file path, looks invalid... Do not use \\, try to use / instead')
            print(argv[1])
            exit(0)

        with open(argv[1], 'r') as file:
            content_to_decode = file.readlines()
    else:
        print("[*] Input Text Mode Selected")
        content_to_decode = [argv[0]]

    print('*************** Decoded Message ***************')
    for line in content_to_decode:
        print(multi_tap_decoder_module.MultiTapDecoder.decode_message(line))
    print('*************** Decoded Message ***************')


if __name__ == '__main__':
    main(sys.argv[1:])
