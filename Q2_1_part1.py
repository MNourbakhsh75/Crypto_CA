import bitcoin.wallet
from bitcoin.core import COIN, b2lx, b2x, lx, serialize, x

from utils import *

bitcoin.SelectParams("testnet")
my_private_key = bitcoin.wallet.CBitcoinSecret("92Gb1F3MyYBY3qGrj5uspgZqsjB1bVGJqFWu8TRichWL1m3Hp3p") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)
# destination_address = bitcoin.wallet.CBitcoinAddress('mko1VJDwt3A3RsqutqGs2BPHB4PyJQLAKF') # Destination address (recipient of the money)

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
                                txout_scriptPubKey_nobody,txout_scriptPubKey_anybody):

    txout_nobody = create_txout(amount_to_send[0], txout_scriptPubKey_nobody)
    txout_anybody = create_txout(amount_to_send[1], txout_scriptPubKey_anybody)

    txin_scriptPubKey = P2PKH_scriptPubKey(my_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, [txout_nobody,txout_anybody], txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, [txout_nobody,txout_anybody], txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)


def P2PKH_scriptPubKey_anybody_or_nobody(anybody):

    if anybody == False:
        return [OP_RETURN]
    else:
        return []


if __name__ == '__main__':
    ######################################################################
    amount_to_send = [0.00050,0.0100]
    txid_to_spend = ('a07062b692690e868c96ccc94354072959d1e28047c2fc86400b799e35c669a1') # TxHash of UTXO
    utxo_index = 0 # UTXO index among transaction outputs
    ######################################################################

    print(my_address) # Prints your address in base58
    print(my_public_key.hex()) # Print your public key in hex
    print(my_private_key.hex()) # Print your private key in hex
    txout_scriptPubKey_nobody = P2PKH_scriptPubKey_anybody_or_nobody(False)
    txout_scriptPubKey_anybody = P2PKH_scriptPubKey_anybody_or_nobody(True)
    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey_nobody,txout_scriptPubKey_anybody)
    print(response.status_code, response.reason)
    print(response.text) # Report the hash of transaction which is printed in this section result
