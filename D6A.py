'''
it needs to report the number of characters from the beginning
of the buffer to the end of the first such four-character marker.

'''
My_File = 'sample.txt'
#My_File = 'D6Ainput.txt'

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
    myset = set()
    # expects the list in reverse order so we can just keep popping off the end.
    # prime the first three entries
    char1 = mylist.pop()
    marker = marker + 1
    char2 = mylist.pop()
    marker = marker + 1
    char3 = mylist.pop()
    marker = marker + 1
    while marker < listlen:
        marker = marker + 1
        char4 = mylist.pop()
        myset = {char1,char2,char3,char4}
        if len(myset) == 4:
            return(marker)
        else:
            char1 = char2
            char2 = char3
            char3 = char4
            char4 = ''


def main():
    load_data()
    for line in inputData:
        linelist = list(line)
        linelist.reverse()
        linemarker = find_start(linelist)
        print(line,'\n',linemarker)


if __name__ == "__main__":
    main()