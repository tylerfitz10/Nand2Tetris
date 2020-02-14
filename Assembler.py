#!/usr/bin/env python3.7

import sys
import os

from address_hash_table import*
from compute_hash_table import*

def symbolTable()


def aHandler(command):
    #pass @i or @sum convert to binary value
    print(f'A Type: {command}')
    command = command.strip('@')
    print(f'{int(command):016b}')

def cHandler(command):

    assemble = {'comp' : None,
                'dest' : 'null',
                'jump' : 'null'}

    #pass instC and return binary value
    #print(f'C Type: {command}')
    #Computation and Jump Only
    if '=' not in command:
        (assemble['comp'], assemble['jump']) = command.split(';')
    #Computation and Destination only
    elif ';' not in command:
        (assemble['dest'],assemble['jump']) = command.split('=')
    #All three fields

    else:
        (assemble['dest'], temp) = command.split('=')
        (assemble['comp'], assemble['jump']) = temp.split(';')

    print(f'dest:{assemble["dest"]}, compt:{assemble["comp"]}, jump:{assemble["jump"]}')

    #return '111' + computations[assemble['comp']] + destinations[assemble['dest']] + jumps[assemble['jump']]


def parseCommand(command):
    # TODO Figure out which type of command and call approriate handler
    #C and A type instructionsDe
    if command[0] == '@':
        aHandler(command)
    elif command[0] == '(':
        print('Found L Type')
    else:
        cHandler(command)

inFile = open(asmFile, 'r')

for line in inFile:

    command = line.split('//')[0].strip()
    if command:

        # todo call parseCommand function
        parseCommand(command)

if __name__ == "__main__":
    
asmFile = sys.argv[1]
#TODO
#try:
    #asmFile

inFile.close()
