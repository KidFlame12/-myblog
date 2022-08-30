from web3 import web3


ganache_url  = "HTTP://127.0.0.1:7545"
web3 = web3(web3.HTTPProvider(ganache_url))

for i in range(0, 4):
    Block_data = web3.eth.getBlock(i)
    print('Block Number:', Block_data['number'])
    print('hash:', Block_data['hash'].hex())
    print('parentHash:', Block_data['parentHash'].hex())
    print('nonce:', Block_data['nonce'].hex())
    print('transaction:', Block_data['transaction'])
    print('----------------------------------------')
    
    
transaction = web3.eth.get_transaction('0x34604FfCc2FC08ac510b24Fb74963B7FcD66655b')
print('transaction data:', transaction)
print('to:', transaction['to'])
print('from:', transaction['from'])
print('value:', transaction['value'])
print('--------------------------------------')