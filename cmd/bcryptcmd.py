#!/usr/bin/python
import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import q4 as bcrpt

parser = argparse.ArgumentParser(prog="bcrypt", description='calculate and cache bcrypt for input')
parser.add_argument('-i', '--input', help='Input file name', required=False)
parser.add_argument('-r', '--rounds', help='Number of rounds to run', required=False, default=18)
parser.add_argument('-d', '--db', help='Database file name', default="bcrypt.cache")
args = parser.parse_args()

if args.input is None:
    tohash = sys.stdin.readline()
else:
    tohash = open(args.input).readline()

crypter = bcrpt.Bcrypter(bcrpt.PickleDriver(args.db))

print crypter.hash(tohash, args.rounds)

crypter.close()
