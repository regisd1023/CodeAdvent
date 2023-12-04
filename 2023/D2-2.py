# template for advent 2023
My_File = 'D2-1data.txt'

#My_File = 'D2sample.txt'

debug=True
debug=False
COLORS = ['red','blue','green']


inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

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
    reds = []
    blues = []
    greens = []

    allgames = chunks[1].split(';')
    for mygame in allgames:
        cubes = mygame.split()
        itercube = iter(cubes)
        for item in itercube:
            mycount = int(item)
            colorend = next(itercube)
            if colorend[-1].isalpha():
                mycolor = colorend
            else:
                mycolor = colorend[:-1]

            if mycolor == 'red':
                reds.append(mycount)
            elif mycolor == 'blue':
                blues.append(mycount)
            elif mycolor == 'green':
                greens.append(mycount)

    if debug:
        print(reds, blues, greens)

    r = max(reds)
    b = max(blues)
    g = max(greens)
    if debug:
        print('red',r,'blue',b,'green',g)
    val = r*b*g

    return(val)



    #return(game)


if __name__ == "__main__":
    main()
