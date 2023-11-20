'''
it needs to report the number of characters from the beginning
of the buffer to the end of the first such four-character marker.

'''
#My_File = 'sample.txt'
My_File = 'D6Ainput.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def find_start(mylist):
    listlen = len(mylist)
    marker = 0
    samplesize = 14
    myset = set()
    # expects the list in reverse order so we can just keep popping off the end.
    # prime the first three entries
    char1 = mylist.pop()
    marker = marker + 1
    char2 = mylist.pop()
    marker = marker + 1
    char3 = mylist.pop()
    marker = marker + 1
    char4 = mylist.pop()
    marker = marker + 1
    char5 = mylist.pop()
    marker = marker + 1
    char6 = mylist.pop()
    marker = marker + 1
    char7 = mylist.pop()
    marker = marker + 1
    char8 = mylist.pop()
    marker = marker + 1
    char9 = mylist.pop()
    marker = marker + 1
    char10 = mylist.pop()
    marker = marker + 1
    char11 = mylist.pop()
    marker = marker + 1
    char12 = mylist.pop()
    marker = marker + 1
    char13 = mylist.pop()
    marker = marker + 1

    while marker < listlen:
        marker = marker + 1
        char14 = mylist.pop()
        myset = {char1, char2, char3, char4, char5, char6, char7, char8, char9, char10,char11, char12, char13, char14}
        if len(myset) == samplesize:
            return(marker)
        else:
            char1 = char2
            char2 = char3
            char3 = char4
            char4 = char5
            char5 = char6
            char6 = char7
            char7 = char8
            char8 = char9
            char9 = char10
            char10 = char11
            char11 = char12
            char12 = char13
            char13 = char14
            char14 = ''


def main():
    load_data()
    for line in inputData:
        linelist = list(line)
        linelist.reverse()
        linemarker = find_start(linelist)
        print(line,'\n',linemarker)


if __name__ == "__main__":
    main()