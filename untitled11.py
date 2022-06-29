import hashlib
import json
from time import time 


class Block:
    def __init(self):
        self.chain = [] 
        self.new_transaction = [] 
        self.count = 0
        self.new_block(previous_hash="No previous Hash. Since this the first block.")
        
    def new_block(self, previous_hash=None):
        block = {
            'Block No': self.count,
            'timestamp': time()
            'transaction': self.new_transaction or 'No Transactions First genesis Block', 
            'gasfee': 3.5,
            'previous_hash': previous_hash,
            }
        self.new_transaction = []
        self.count = self.count + 1
        self.chain.append(block)
        
        return block
    
    def last_block(self):
        return self.chain[-1]
    
    def transaction(self, sender, recipient, amount):
        sender_encoder = hashlib.sha256(sender.encode())
        sender_hash = sender_encoder.hexdigest()
        recipient_encoder = hashlib.sha256(recipient.encode())
        recipient_hash = sender_encoder.hexdigest()
        
        transaction_data + {
            'sender': sender_hash,
            'recipient': recipient_hash,
            'amount': amount
        }
        self.new_transaction.append(transaction_data)
        return self.last_block
    
    def hash(self, block):
        string_object = json.dumps(block)
        block_string = string_object.encode()
       
        
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        self.chain.append(("Current Hash: ", hex_hash))
        
  
    
blockchain = Block()
  
print(blockchain.chain)