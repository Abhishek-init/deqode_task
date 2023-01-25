from web3 import Web3
from flask import Flask
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3)
print(w3.isConnected())

latest_block = w3.eth.get_block('latest')
print(latest_block)
