import hashlib

SALT = 'ngcjuoqr'


def multihash(s, n):
    hash = hashlib.md5((SALT+str(index)).encode()).hexdigest()
    for i in range(n):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash


index = 0
prefinish_index = 0
keys = []
candidates = {}
enough = False
while True:
    hash = multihash(SALT+str(index), 2016)
    quintlets = set()
    for j in range(len(hash)-4):
        if hash[j:j+5] == hash[j]*5:
            quintlets.add(hash[j])
    to_purge = []
    for candidate_hash, candidate_data in candidates.items():
        candidate_index, candidate_symbol = candidate_data
        if index - candidate_index > 1001:
            to_purge.append(candidate_hash)
            continue
        if candidate_symbol in quintlets:
            keys.append((candidate_index))
            to_purge.append(candidate_hash)
    for hash_to_purge in to_purge:
        del candidates[hash_to_purge]
    for j in range(len(hash)-2):
        if hash[j:j+3] == hash[j]*3:
            candidates[hash] = (index, hash[j])
            break
    index += 1
    if len(keys) > 64 and not prefinish_index:
        prefinish_index = index
    if prefinish_index and index - prefinish_index > 1001:
        break

keys.sort()
print(keys[63])
