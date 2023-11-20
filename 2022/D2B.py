'''

'''
#My_File = 'sample.txt'
My_File = 'D2Adata.txt'

playdict = {
    'A' : 'rock',
    'B' : 'paper',
    'C' : 'scissors',
    'X' : ['lose',0],
    'Y' : ['draw',3],
    'Z' : ['win',6],
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3
}
inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def roshambo(elfshape,outcome):
    if outcome == 'win':
        if elfshape == 'rock':
            return('paper')
        if elfshape == 'paper':
            return ('scissors')
        if elfshape == 'scissors':
            return ('rock')

    if outcome == 'lose':
        if elfshape == 'rock':
            return('scissors')
        if elfshape == 'paper':
            return ('rock')
        if elfshape == 'scissors':
            return ('paper')

    if outcome == 'draw':
        return(elfshape)
    return(False)

def run_turn(elfplay,myplay):
    turnscore = 0
    wld = playdict[myplay]
    print('wld',wld,' elfplay',playdict[elfplay])
    myshape = roshambo(playdict[elfplay],wld[0])
    turnscore = turnscore + wld[1]
    turnscore = turnscore + playdict[myshape]
    return(turnscore)

def main():
    load_data()
    totalscore = 0
    for line in inputData:
        play = line.split()
        elf = play[0]
        wld = play[1]
        turnscore = run_turn(elf,wld)
        totalscore = totalscore + turnscore
        #print(totalscore)
    print('total ',totalscore)


if __name__ == "__main__":
    main()