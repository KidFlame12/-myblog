from web3 import web3
from web3.midddleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3 = web3(web3.HTTPProvider(API_url))

Block_data = web3.eth.getblock(13054520)


transaction = web3.eth.get_transaction('')

print('blockHash:',transaction['blockHash'].hex())
print('blockNumber:',transaction['blockNumber'])
print('from:',transaction['from'])
print('gas:',transaction['gas'])
print('gasprice in either:',transaction['gasprice'])
print('hash:',transaction['hash'].hex)
print('input:',transaction['input'])
print('nonce:',transaction['nonce'])
print('signature:',transaction['s'].hex())
print('to:',transaction['to'])
print('value:',transaction['value'])