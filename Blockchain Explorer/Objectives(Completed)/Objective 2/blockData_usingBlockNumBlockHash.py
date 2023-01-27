import json
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware

#Getting block data using block number & block Hash
def get_block_data_num(block_number):
    # w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
    w3 = Web3(Web3/HTTPProvider('httpd://127.0.0.1:8545)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    Block_data_using_num = w3.eth.get_block(block_number)  #Using Block Number
    print(Block_data_using_num)

block_number = int(input("Enter Block Number: "))
get_block_data_num(block_number)

print("\n")

def get_block_data_hash(block_hash):
   w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
   w3.middleware_onion.inject(geth_poa_middleware, layer=0)

   #Hash Valuse:    '0x55a2d76a8c181f5ff01efc382aea84a8e886172999459c0f83bd1ba6f57a8d6e'
   Block_data_using_hash = w3.eth.get_block(block_hash)  #Using Block Hash
   print(Block_data_using_hash)

block_hash = input("Enter Block Hash: ")
get_block_data_hash(block_hash)

print("\n")

#------------------------------------------------------------------------------------------------------------------------

#Getting Transaction data using transaction hash:

#'0x1287bce9d76712f6410c585e1921056f1abfc98c9bb8b57680873de561160234'
def get_transaction_data(transaction_hash):
    w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    Transaction_data = w3.eth.get_transaction(transaction_hash)  #Using Transaction Hash
    print(Transaction_data)

transaction_hash =  input("Enter Transaction Hash: ")
get_transaction_data((transaction_hash))
