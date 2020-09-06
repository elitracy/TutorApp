import hashlib

thing = 'Lefty7518'

hash_object = hashlib.md5(thing.encode())
print(hash_object.hexdigest())