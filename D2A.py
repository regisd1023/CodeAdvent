'''

'''
My_File = 'D2Adata.txt'

playdict = {
    'A' : ['rock',1],
    'B' : ['paper',2],
    'C' : ['scissors',3],
    'X' : ['rock',1],
    'Y' : ['paper',2],
    'Z' : ['scissors',3]
}
inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def roshambo(elfshape,myshape):
    if elfshape == myshape:
        return(3)
    if elfshape == 'rock':
        if myshape == 'paper':
            return(6)
        elif myshape == 'scissors':
            return(0)
        return(False)
    if elfshape == 'paper':
        if myshape == 'scissors':
            return(6)
        elif myshape == 'rock':
            return(0)
        return(False)

    if elfshape == 'scissors':
        if myshape == 'rock':
            return (6)
        elif myshape == 'paper':
            return (0)
        return (False)
    return(False)

def run_turn(elfplay,myplay):
    turnscore = 0
    playscore = roshambo(playdict[elfplay][0],playdict[myplay][0])
    #print (playscore)
    return(playscore)

def main():
    load_data()
    totalscore = 0
    for line in inputData:
        play = line.split()
        elf = play[0]
        mine = play[1]
        totalscore = totalscore + run_turn(elf,mine)
        totalscore = totalscore + playdict[mine][1]
        print(totalscore)
    print('total ',totalscore)


if __name__ == "__main__":
    main()