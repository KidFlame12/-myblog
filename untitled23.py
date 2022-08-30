from web3 import web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3_ganache_connection =web3(web3.HTTPProvider(ganache_url))

Bradley_account = '0x5011E6C21cF24705dB85527F8b7c34A732137d1B'
Khami_account = '0x27d09c7601Ef6ca445Ac4700DC487C2AeA81c815'

nonce = web3_ganache_connection.eth.getTransactionCount(Alice_account)
transaction_data = {
    'nonce':nonce,
    'to':Bradley_account
    'value':web3_ganache_connection.toWei(20,'ether')
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(0.000525,'gwei')
}
private_key = '5ad42050a587c9fad6dfc0de4ebfddbf4206cdca7c429dc345e0e2f4ff873b21'
signed_transaction = web3_ganache_connection.eth.account.signTransaction(transaction_data,private_key)
transaction_hash = web3_ganache_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)


print(web3_ganache_connection.tohex(transaction_hash))
