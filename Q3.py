import codecs
import datetime
import json
import time
from datetime import timezone

from Q1_1 import perform_sha256


def convert_to_LEnidan(val,width):
    bytes = val.to_bytes(width,byteorder='little')
    return bytes.hex()

def get_block_height(height):

    width = (height.bit_length() + 7) // 8
    return convert_to_LEnidan(height,width)

def swap_endian(val):

    return codecs.encode(codecs.decode(val, 'hex')[::-1], 'hex').decode()

def create_coinbase_transaction(height):

    version = '01000000'
    input_count = '01'
    tx_id = '0'*64
    v_out = 'ffffffff'
    #810100495MehrdadNourbakhsh
    coinbase_data = '3831303130303439354d6568726461644e6f757262616b687368'
    scriptSig = '02' + get_block_height(height) + coinbase_data
    scriptSig_size = convert_to_LEnidan(int(len(scriptSig)/2),1)
    sequence = 'ffffffff'
    output_count = '01'
    #current reward = 6.25683447 BTC
    coinbase_value = convert_to_LEnidan(625683447,8)
    public_key_hash160 = 'a7452f0d1f27649c3b4bcadc55e2926d89e38576'
    scriptPubKey = '76' + 'a9' + '14' + public_key_hash160 + '88' + 'ac'
    scriptPubKey_size = convert_to_LEnidan(int(len(scriptPubKey)/2),1)
    lock_time = '00000000'

    coinbase = version + input_count + tx_id + v_out + scriptSig_size + scriptSig + sequence + output_count + coinbase_value + scriptPubKey_size + scriptPubKey + lock_time
    return coinbase

def get_merkle_root(transaction):

    tx_id = perform_sha256(perform_sha256(transaction))
    return tx_id


def get_unix_time():

    date_time = datetime.datetime(tzinfo=timezone.utc,year = 2022, month = 12, day = 28, hour = 10, minute= 10,second = 30)
    unix_time = datetime.datetime.timestamp(date_time)
    unix_time_hex = convert_to_LEnidan(int(unix_time),4)
    return unix_time_hex

def get_target(difficulty):

    prefix = '0'*difficulty
    mantissa = '00ffff'
    len_exponent = 64 - (len(prefix) + len(mantissa))
    exponent = '0'*len_exponent
    target = prefix + mantissa + exponent
    return target

def create_block_header(root,pb):

    header = {}
    header['version'] = '01000000'
    header['merkle_root'] = root
    header['prev_block'] = pb
    header['time'] = get_unix_time()
    header['bits'] = 'ffff001e'

    return header


def mining(header,target):

    print('Mining...')
    start = time.time()
    max_nonce = 1000000000
    serialized_header = header['version'] + header['prev_block'] + header['merkle_root'] + header['time'] + header['bits']
    for nonce in range(0,max_nonce):
        nonce_hex = convert_to_LEnidan(nonce,4)
        block_serialized = serialized_header + nonce_hex
        block_hash = perform_sha256(perform_sha256(block_serialized))
        block_hash = swap_endian(block_hash)
        if int(block_hash,16) < int(target,16):
            end = time.time()
            delta = "{:.2f}".format((end-start)/60)
            print('Block was found after ',delta,' minutes')
            return block_hash,block_serialized,nonce

    return print('No Block Found...')

def human_readable_block(header,block_hash,nonce,height):

    data = dict()
    data = {
        'hash': block_hash,
        'version:' : 1,
        'height:' : height,
        'block_reward:' : 625683447,
        'merkle_root:' : swap_endian(header['merkle_root']),
        'time:': datetime.datetime.utcfromtimestamp(int(swap_endian(header['time']),16)).strftime('%Y-%m-%d %H:%M:%S'),
        'bits:': swap_endian(header['bits']),
        'previous_block_hash': swap_endian(header['prev_block']),
        'nonce:' : nonce,
        'nTx:': 1,
        'tx:':[swap_endian(header['merkle_root'])]
    }
    return data

def get_raw_block(block_serialized,coinbase_transaction):

    raw_block = block_serialized + '01' + coinbase_transaction
    return raw_block


if __name__ == '__main__':

    height = 496
    #hash of block 495
    prev_block = '00000000e47349de5a0193abc5a2fe0be81cb1d1987e45ab85f3289d54cddc4d'

    coinbase_transaction = create_coinbase_transaction(height)
    merkle_root = get_merkle_root(coinbase_transaction)
    block_header = create_block_header(merkle_root,swap_endian(prev_block))
    difficulty = 4
    target = get_target(difficulty)
    block_hash,block_serialized,nonce = mining(block_header,target)
    print('Block Hash: ',block_hash)
    print('Block Raw:',get_raw_block(block_serialized,coinbase_transaction))
    data = human_readable_block(block_header,block_hash,nonce,height)
    print(json.dumps(data, indent=4))
    
    