# template for advent 2023

debug=True
#debug=False

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
    trim1 = mytext.split(':')[1]
    trim2 = trim1.split('|')
    winstring = trim2[0].split()
    minestring = trim2[1].split()
    for x in winstring:
        winning.append(int(x))
    for y in minestring:
        mine.append(int(x))
    card_lists = [winning, mine]
    return(card_lists)



def check_card(myline):
    cardsections = []
    cardsections = cardsanitize(myline)









def main():
    load_data()


if __name__ == "__main__":
    main()
