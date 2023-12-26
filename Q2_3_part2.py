import bitcoin.wallet
from bitcoin.core import COIN, b2lx, b2x, lx, serialize, x

from utils import *

bitcoin.SelectParams("testnet")
my_private_key = bitcoin.wallet.CBitcoinSecret("923KepUM6nFCyPJ18hyuYCsE4vBLeWRiLHyaS2qbxVw9SHWEmS5") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)
destination_address = bitcoin.wallet.CBitcoinAddress('mtkBYwwQpaCCS1uvWwWpFRdA1XKME1DkpQ') # Destination address (recipient of the money)

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

def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,txout_scriptPubKey):

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey_Primes()
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig_Primes()

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,txin_scriptSig)

    return broadcast_transaction(new_tx)


def P2PKH_scriptPubKey_Primes():

    opcodes = [OP_2DUP,OP_ADD, OP_16, OP_EQUALVERIFY,OP_SUB,OP_6,OP_EQUAL]
    return opcodes

def P2PKH_scriptSig_Primes():

    return [OP_11,OP_5]

if __name__ == '__main__':
    
    amount_to_send = 0.0161
    txid_to_spend = ('87ef09f66e56847d5424312caad38d1b33069646f1d1037e9344a65c311e1f8b') # TxHash of UTXO
    utxo_index = 0 # UTXO index among transaction outputs
    

    print(my_address) # Prints your address in base58
    print(my_public_key.hex()) # Print your public key in hex
    print(my_private_key.hex()) # Print your private key in hex
    txout_scriptPubKey = P2PKH_scriptPubKey(destination_address)
    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text) # Report the hash of transaction which is printed in this section result
