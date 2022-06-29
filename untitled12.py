from web3 import web3
from web3.midddleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3 = web3(web3.HTTPProvider(API_url))

Block_data = web3.eth.getblock(12964964)
print('Block data:',Block_data )

print('gasused:',Block_data  ['gasused'])
print('Total Difficulty',Block_data ['difficulty'])

print('transaction data',Block_data ['transactions'])
transaction = web3.eth.get_transaction('')
print('data',transaction  )