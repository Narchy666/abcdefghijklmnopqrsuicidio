import random
import hashlib
import hmac
from passwords import Password

def hash_algo():
    hashtype = int(input("enter the number corresponding to the desired hash algorithm: \n"
                         "1)sha1\n2)sha224\n3)sha256\n4)sha384\n5)sha512\n6)md5\n7)blake2b\n8)blake2s\n"))
    if hashtype == 1:
        hashtype = hashlib.sha1
    elif hashtype == 2:
        hashtype = hashlib.sha224
    elif hashtype == 3:
        hashtype = hashlib.sha256
    elif hashtype == 4:
        hashtype = hashlib.sha384
    elif hashtype == 5:
        hashtype = hashlib.sha512
    elif hashtype == 6:
        hashtype = hashlib.md5
    elif hashtype == 7:
        hashtype = hashlib.blake2b
    elif hashtype == 8:
        hashtype = hashlib.blake2s
    else:
        raise Exception("invalid hash algorithm please select using one of the above using the respective number")
    return hashtype


def get_random_msg():
    message = ''.join((random.choice("!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';") for i in range(32)))
    return message


def get_pwd():
    password = input("enter your password: ")
    return password


def pwd_length():
    length = int(input("enther the desired length of the hashed password: "))
    return length


def hash_pwd(password, message, length, hashtype):
    hashed_pwd = hmac.new(bytes(password, 'UTF-8'), msg=bytes(message, 'UTF-8'), digestmod=hashtype).hexdigest()
    return hashed_pwd[:length]


def website():
    website = input("enter the website you want to use this password on: ")
    return website

def write_file():
    with open("pwds.txt", "a") as f:
        f.write("---------------------\n")
        f.write(f"Website: {password.website}\n")
        f.write(f"Hashed password: {password.hashtype}\n")
        f.write(f"Unhashed password: {password.password}\n")
        f.write(f"hmac msg: {password.message}\n")
        f.write("---------------------\n")

if __name__ == "__main__":
    website = website()
    pwd = get_pwd()
    message = get_random_msg()
    pwdlen = pwd_length()
    hashedpwd = hash_pwd(pwd, message, pwdlen, hash_algo())

    password = Password(website, pwd, message, pwdlen, hashedpwd)
    write_file()