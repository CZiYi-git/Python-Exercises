import hashlib
import os


def hash_value(value: str, salt: str):
    salt = bytes(salt, encoding='utf-8')
    value = value.encode('utf-8')
    hash_obj = hashlib.pbkdf2_hmac('sha256', value, salt, 100000)
    hash = hash_obj.hex()
    return hash


def check_value(value, hashed_value, salt):
    salt = bytes(salt, encoding='utf-8')
    value = value.encode('utf-8')
    new_hash_obj = hashlib.pbkdf2_hmac('sha256', value, salt, 100000)
    new_hash = new_hash_obj.hex()
    if new_hash == hashed_value:
        return True
    else:
        return False


def hash_list(li: list[str], salt):
    t = []
    for s in li:
        t.append(hash_value(s, salt))
    return t


def txt_to_hashlist(path):
    f = open(path, 'r')
    return [i.replace('\n', '') for i in f.readlines()]


