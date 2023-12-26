import codecs
import hashlib
import secrets

import base58check
import ecdsa


def perform_ripemd160(input_str):

    hex_str = bytearray.fromhex(input_str)
    ripemd = hashlib.new('ripemd160')
    ripemd.update(hex_str)
    hashed = ripemd.hexdigest()
    return hashed

def perform_sha256(input_str):

    hex_str = bytearray.fromhex(input_str)
    sha = hashlib.sha256()
    sha.update(hex_str)
    hashed = sha.hexdigest()
    return hashed


def generate_private_key():

    flag = False
    while flag != True:
        bits = secrets.randbits(256)
        private_key = hex(bits)[2:]
        if len(private_key) == 64:
            flag = True
    return private_key

def convert_to_wif(key,compressed = False):

    extend_key = 'ef' + key
    if compressed == True:
        extend_key = extend_key + '01'
    hashed_key = perform_sha256(perform_sha256(extend_key))
    checksum = hashed_key[0:8]
    extended_checksum = extend_key + checksum
    wif_private_key = base58check.b58encode(bytes(bytearray.fromhex(extended_checksum))).decode('utf-8')
    return wif_private_key


def generate_public_key(private_key):

    private_key_bytes = bytearray.fromhex(private_key)
    public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    public_key_bytes = public_key_raw.to_string()
    public_key = '04' + public_key_bytes.hex()
    return public_key

def generate_testnet_address(public_key):

    hashed_key = perform_ripemd160(perform_sha256(public_key))
    extend_hashed_key = '6f' + hashed_key
    checksum = perform_sha256(perform_sha256(extend_hashed_key))[0:8]
    extended_checksum = extend_hashed_key + checksum
    address = base58check.b58encode(bytes(bytearray.fromhex(extended_checksum))).decode('utf-8')
    return address

if __name__ == '__main__':

    pr_key = generate_private_key()
    print('Private Key: ',pr_key)
    print('Private Key(WIF Format): ',convert_to_wif(pr_key))
    pub_key = generate_public_key(pr_key)
    address = generate_testnet_address(pub_key)
    print('Address: ',address)
