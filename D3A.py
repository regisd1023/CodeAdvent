'''
base to load data and run main.
'''
My_File = 'D3Atext.txt'

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
    for line in inputData:
        linelen = len(line)
        splitpoint = int(linelen/2)
        firstcompartment = line[:splitpoint]
        secondcompartment = line[splitpoint:]
        common = findcommon(firstcompartment,secondcompartment)
        if len(common) != 1:
            print('wat')
            return(False)
        total = total + get_letterval(common)
        print(total)


if __name__ == "__main__":
    main()