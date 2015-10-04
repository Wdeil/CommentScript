#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib


def EncryMd5(plaintext):
	return hashlib.md5((plaintext.encode('utf-8'))).hexdigest()

def EncrySha1(plaintext):
	return hashlib.sha1(plaintext.encode('utf-8')).hexdigest()

def EncrySha224(plaintext):
	return hashlib.sha224(plaintext.encode('utf-8')).hexdigest()

def EncrySha256(plaintext):
	return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()

def EncrySha384(plaintext):
	return hashlib.sha384(plaintext.encode('utf-8')).hexdigest()

def EncrySha512(plaintext):
	return hashlib.sha512(plaintext.encode('utf-8')).hexdigest()


if __name__ == '__main__':
	t = input('1:md5;\n2:sha1;\n3:sha224;\n4:sha256;\n5:sha384;\n6:sha512;\nEnter your choice: ')
	plaintext = input('Enter Your Plaintext: ')
	if t == '1':
		print(EncryMd5(plaintext))
	elif t == '2':
		print(EncrySha1(plaintext))
	elif t == '3':
		print(EncrySha224(plaintext))
	elif t == '4':
		print(EncrySha256(plaintext))
	elif t == '5':
		print(EncrySha384(plaintext))
	elif t == '6':
		print(EncrySha512(plaintext))
	else :
		print("Choice Erorr!")
