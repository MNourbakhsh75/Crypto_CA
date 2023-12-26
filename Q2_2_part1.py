import bitcoin.wallet
from bitcoin.core import COIN, b2lx, b2x, lx, serialize, x

from utils import *

bitcoin.SelectParams("testnet")
my_private_key = bitcoin.wallet.CBitcoinSecret("92s5aqabZJm6zpFvt5mw8q8zomYU5eAcHjEHgQtAWKmWJz5n7zv") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)

private_key_1 = bitcoin.wallet.CBitcoinSecret("91v52oZahQ6FqwAm2UPc7Pa7a4F5a17vYmfxe57VfcnpF8gxx9u")
private_key_2 = bitcoin.wallet.CBitcoinSecret("925p3VWjzwareVptwSGgg1QNRoH3VzxjmTpRNHVnwZbQLTgvA6e")
private_key_3 = bitcoin.wallet.CBitcoinSecret("92U5odwr1y2MdYjizqB1Rcdcycb65HRj51UbzeYsiWaQzFshVkd")
public_key_1 = private_key_1.pub
public_key_2 = private_key_2.pub
public_key_3 = private_key_3.pub

def P2PKH_scriptPubKey(address):
    ######################################################################
    ## Fill out the operations for P2PKH scriptPubKey                   ##

    return [ OP_DUP , OP_HASH160 ,address , OP_EQUALVERIFY  ,OP_CHECKSIG]
    ######################################################################

def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    ######################################################################
    ## Fill out the operations for P2PKH scriptSig                      ##

    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)

    return [signature , my_public_key] #Fill this section
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(my_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

def P2MS_scriptPubKey(pub_1, pub_2, pub_3):

    return [OP_2, pub_1, pub_2, pub_3, OP_3 , OP_CHECKMULTISIG]

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.0122
    txid_to_spend = ('5ad54c975b61aa1b85262836b565128bd1a0644e8760d39fe5675d8637608fce') # TxHash of UTXO
    utxo_index = 1 # UTXO index among transaction outputs
    ######################################################################

    print(my_address) # Prints your address in base58
    print(my_public_key.hex()) # Print your public key in hex
    print(my_private_key.hex()) # Print your private key in hex
    txout_scriptPubKey = P2MS_scriptPubKey(public_key_1,public_key_2,public_key_3)
    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text) # Report the hash of transaction which is printed in this section result
