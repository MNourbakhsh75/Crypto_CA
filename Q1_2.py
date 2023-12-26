from Q1_1 import *


def generate_vanity_address(chars):

    while True:
        private_key = generate_private_key()
        public_key = generate_public_key(private_key)
        address = generate_testnet_address(public_key)
        if address.startswith('m'+chars) or address.startswith('n'+chars):
            return convert_to_wif(private_key),address


if __name__ == '__main__':

    chars = input()
    pr_key,address = generate_vanity_address(chars)
    print('Private Key(WIF Format): ',pr_key)
    print('Address: ',address)
