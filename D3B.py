'''
base to load data and run main.
'''
My_File = 'D3Atext.txt'
#My_File = 'sample.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def findcommon(list1,list2):
    result = ''
    seta = set(list1)
    setb = set(list2)
    common = seta&setb
    if len(common) > 0:
        result = list(common)[0]
    return(result)

def findcommon3(list1,list2,list3):
    result = ''
    seta = set(list1)
    setb = set(list2)
    setc = set(list3)
    common = seta & setb & setc
    if len(common) > 0:
        result = list(common)[0]
    return(result)


def get_letterval(x):
    my_val = ord(x) - 64
    if my_val < 27:
        my_val = my_val + 26
        return(my_val)
    else:
        my_val = my_val - 32
        return(my_val)

def main():
    load_data()
    total = 0
    numlines = len(inputData)
    print(numlines)
    linemarker = 0
    while linemarker < (numlines - 2):
        elf0 = inputData[linemarker]
        elf1 = inputData[linemarker + 1]
        elf2 = inputData[linemarker + 2]
        x = findcommon3(elf0,elf1,elf2)
        myval = get_letterval(x)
        print(x,myval)
        total = total + myval
        print(total)
        linemarker = linemarker + 3


if __name__ == "__main__":
    main()