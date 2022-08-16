from web3 import web3


ganache_url  = "HTTP://127.0.0.1:7545"
web3 = web3(web3.HTTPProvider(ganache_url))

account1 = '0x5cB88FEEFCa30E7FDf85B44037C84D9742617990'
account2 = '0x661b6C6FD8912A4b6850A4Dd340Bf870f2Aca92B'

private_key = '0x49D4Ba56e7246D8D79ae40E5F7a47A2849a22188'


nonce = wen3.eth.getTransactionCount(account1)

tx = {
      'nonce':nonce,
      'to':account2,
      'value':web.towei(1, 'ether'),
      'gas':21000,
      'gasPrice':web3.towei(50,'gwei')
      }

singed_tx = web3.eth.account.signTransaction(tx,private_key)
tx_hash = web3.eth.sendRawTransaction(singed_tx.rawTRansaction)

print(web3.toHex(tx_hash  ))