import hashlib

minha_hash = hashlib.sha256(b'ufscar').hexdigest()

# minha_hash = hashlib.sha256(b'universidade federal de sao carlos').hexdigest()

print(minha_hash)
