#!/usr/bin/env python3.7

import sys
import os

from address_hash_table import*
from compute_hash_table import*
from label_hash_table import*

def lHandler(command):
    label = command.strip()
    print(f'lHandler')
    

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


def parseCommand(command):
    # TODO Figure out which type of command and call approriate handler
    #C and A type instructionsDe
    if command[0] == '@':
        aHandler(command)
    elif command[0] == '(':
        lHandler(command)
    else:
        cHandler(command)



if __name__ == "__main__":

    asmFile = str(sys.argv[1])

    inFile = open(asmFile, 'r')

    for line in inFile:

        command = line.split('//')[0].strip()

        if command:

        # todo call parseCommand function
            parseCommand(command)
    #asmFile



inFile.close()
"""
lHandler
A Type: @0
0000000000000000
dest:D, compt:None, jump:M
A Type: @1
0000000000000001
dest:D, compt:None, jump:D-M
A Type: @10
0000000000001010
dest:null, compt:D, jump:JGT
A Type: @1
0000000000000001
dest:D, compt:None, jump:M
A Type: @12
0000000000001100
dest:null, compt:0, jump:JMP
A Type: @0
0000000000000000
dest:D, compt:None, jump:M
A Type: @2
0000000000000010
dest:M, compt:None, jump:D
A Type: @14
0000000000001110
dest:null, compt:0, jump:JMP
dest:M, compt:D, jump:JMP"""
