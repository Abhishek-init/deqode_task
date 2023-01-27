# Import Essential lib #web3
from web3 import Web3
from web3.middleware import geth_poa_middleware

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3)
print(w3.isConnected())

block_number = w3.eth.blockNumber
# Get the block data for the latest block
Block_data = w3.eth.get_block(block_number)
print("Block Number: ", block_number)
print(Block_data)
# print("Block Hash: ", block['hash'])
# print("Block Timestamp: ", block['timestamp'])
# print("Block Transactions: ", block['transactions'])
