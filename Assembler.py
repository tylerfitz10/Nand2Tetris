import sys

def aHandler()
    #pass @i or @sum convert to binary value

def cHandler()
    #pass instC and return binary value
    #Computation and Jump Only
    #Desination and Jump only
    #All three fields

def parseCommand(command):
    # TODO Figure out which type of command and call approriate handler
    #C and A type instructions

asmFile = sys.argv[1]

inFile = open(asmFile, 'r')

for line in inFile:

    command = line.split('//')[0].strip()
    if command:
        print(command)
        # todo call parseCommand function
        parseCommand(command)

inFile.close()
