import json
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware

#Getting Transaction data using transaction hash:
#'0x1287bce9d76712f6410c585e1921056f1abfc98c9bb8b57680873de561160234'

def get_transaction_data(transaction_hash):
    w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    Transaction_data = w3.eth.get_transaction(transaction_hash)  #Using Transaction Hash
    print(Transaction_data)

transaction_hash =  input("Enter Transaction Hash: ")
get_transaction_data((transaction_hash))