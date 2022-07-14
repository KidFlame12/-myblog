from web3 import web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3 = web3(web3.HTTPProvider(infura_url))

req_ethgas_data = request.get('https://ethgasstation.info/json/ethgasAPI.json')



print('safelow', trans_info['safelow])
print('average', trans_info['average'])
print('fast', trans_info['fast'])
print('fastest', trans_info['fastest'])
print('block Number:', tran_info['blockNum'])


gas_price = web3.eth.gasPrice
print('Calculated gas price:', gas_price/10**9)
