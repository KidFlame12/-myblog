import hashlib

text1 = "I am a genius, smater than Einstein himself."
result = hashlib.sha3_256(text.encode())

print("The SHA256 of text 1 is: ",result.hexdigest())
 
text2 = "  No your not the genius,I am genius,  I am smater than him."
result = hashlib.sha3_256(text.encode())

print("The SHA256 of text 2 is: ",result.hexdigest())
 