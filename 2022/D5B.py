'''
base to load data and run main.
'''
My_File = 'D5A.txt'

inputData = []
# stacks = {1:['[Z]','[N]'],2:['[M]','[C]','[D]'],3:['[P]']}
stacks = {
0: ['null'],
1: ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
2: ['V', 'W', 'J'],
3: ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
4: ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
5: ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
6: ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
7: ['D', 'H', 'G', 'M', 'R'],
8: ['H', 'N', 'M', 'V', 'Z', 'D'],
9: ['G', 'N', 'F', 'H']
}

numStack = 9 #number of stacks

def load_data():
    fhand = open(My_File)
    for line in fhand:
        #inputData.append(line.rstrip())
        inputData.append(line.rstrip('\r\n'))
    fhand.close()
    return()

def crateMove(off,on):
    crate = stacks[off].pop()
    print('crate',crate)
    stacks[on].append(crate)
    return(True)

def do_instr(myline):
    words = myline.split()
    if len(words) != 6:
        print('do_instr wat')
        return(False)
    numCrates = int(words[1])
    offstack = int(words[3])
    onstack = int(words[5])
    print('popping',numCrates,'from',offstack,'to',onstack)
    loopcount = 0
    while loopcount < numCrates:
        print('moving crate',(loopcount + 1))
        print('off\t',stacks[offstack],'\non\t',stacks[0])
        crateMove(offstack,0)
        print('off\t',stacks[offstack],'\non\t',stacks[0])
        loopcount = loopcount + 1
    loopcount = 0
    while loopcount < numCrates:
        print('moving crate',(loopcount + 1))
        print('off\t',stacks[0],'\non\t',stacks[onstack])
        crateMove(0,onstack)
        print('off\t',stacks[0],'\non\t',stacks[onstack])
        loopcount = loopcount + 1

    return(True)

def main():
    load_data()
    rawStack = []
    rawInst = []
    inStack = True
    inInstr = False
    for line in inputData:
        if len(line) == 0:
            if inStack and (not inInstr):
                inStack = False
                inInstr = True
                continue
        elif inStack:
            #rawStack.append(line + ' ')
            rawStack.append(line)
        elif inInstr:
            rawInst.append(line)
        else:
            return(False)

    for instr in rawInst:
        print(instr)
        do_instr(instr)

    for stacklist in stacks.values():
        print(stacklist)

    myresult = ''
    for stack in stacks:
        myresult = myresult + stacks[stack].pop()
    print(myresult)

if __name__ == "__main__":
    main()


'''

    for instr in rawInst:
        do_instr(instr)


stacks = {
1: ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
2: ['D', 'W', 'B'],
3: ['T', 'S', 'Q', 'W', 'J', 'C'],
4: ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
5: ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
6: ['B', 'W', 'F', 'T', 'N'],
7: ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
8: ['H', 'P', 'F', 'R'],
9: ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
}
'''