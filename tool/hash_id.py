import hashlib
import sys

def identify_hash(hash):
    hash_types = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
        'sha224': hashlib.sha224,
        'sha384': hashlib.sha384
    }
    for name, func in hash_types.items():
        try:
            if func().hexdigest() == hash:
                print(f'Hash type: {name}')
                return
        except:
            pass
    print('Hash type not recognized')

if __name__ == '__main__':
    identify_hash(sys.argv[1])
