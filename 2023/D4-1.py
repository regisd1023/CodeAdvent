# template for advent 2023

debug=True
debug=False
My_File = 'D4-data.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def cardsanitize(mytext):
    # assuming I get something like this:
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # returning [list1, list2] for the two lists of numbers
    trim2 = []
    card_lists = []
    winning = []
    mine = []
    if debug:
        print(mytext)
    trim1 = mytext.split(':')[1]
    trim2 = trim1.split('|')
    winstring = trim2[0].split()
    minestring = trim2[1].split()
    for x in winstring:
        winning.append(int(x))
    for y in minestring:
        mine.append(int(y))
    card_lists = [winning, mine]
    if debug:
        print(card_lists)
    return(card_lists)


def check_card(myline):
    cardvalue = 0
    cardsections = []
    cardsections = cardsanitize(myline)
    for mynum in cardsections[0]:
        if debug:
            print(mynum)
        if mynum in cardsections[1]:
            if cardvalue == 0:
                cardvalue = 1
            else:
                cardvalue = cardvalue * 2
    return(cardvalue)



def main():
    rawcards = []
    load_data()
    card_total = 0
    for card in inputData:
        print(card)
        x=check_card(card)
        print(x)
        card_total = card_total + x
    print('total ',card_total)

if __name__ == "__main__":
    main()
