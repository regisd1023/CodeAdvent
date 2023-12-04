# template for advent 2023
My_File = 'D2-1data.txt'

#My_File = 'D2sample.txt'

debug=True
debug=False
COLORS = ['red','blue','green']

# 12 red cubes, 13 green cubes, and 14 blue cubes
MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

LIMITS = {'red':MAXRED,'green':MAXGREEN,'blue':MAXBLUE}

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def testred(x):
    if x > MAXRED:
        if debug:
            print('red fail')
        return(False)
    else:
        if debug:
            print('red good')
        return(True)
def testgreen(x):
    if x > MAXGREEN:
        if debug:
            print('green fail')
        return(False)
    else:
        if debug:
            print('green good')
        return(True)
def testblue(x):
    if x > MAXBLUE:
        if debug:
            print('blue fail')
        return(False)
    else:
        if debug:
            print('blue good')
        return(True)

def testcube(myc,myn):
    if myc == 'red':
        return(testred(myn))
    elif myc == 'blue':
        return(testblue(myn))
    else:
        return(testgreen(myn))

def main():
    load_data()
    totalvalue = 0
    for item in inputData:
        itemval = parse_line(item)
        print(itemval)
        totalvalue = totalvalue + itemval
    print('total: ',totalvalue)

    return()



def parse_line(mystring):
    countline = True
    # expect line like "game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    cubedict = dict()
    chunks = mystring.split(':')
    gamestr = chunks[0].split()[1]
    game = int(gamestr)

    games = chunks[1].split(';')
    for mygame in games:
        # initialize
        cubedict = {'blue': 0, 'red': 0, 'green': 0}

        cubes = mygame.split()
        itercube = iter(cubes)
        for item in itercube:
            mycount = int(item)
            colorend = next(itercube)
            if colorend[-1].isalpha():
                mycolor = colorend
            else:
                mycolor = colorend[:-1]
            cubedict[mycolor] = cubedict.get(mycolor) + mycount
        if debug:
            print(cubedict)
        for c in COLORS:
            if not (testcube(c,cubedict[c])):
                print('game', game,'impossible')
                return(0)


    print('game',game,'possible')

    return(game)



    #return(game)


if __name__ == "__main__":
    main()
