
debug = True
debug = False

My_File = 'D1input.txt'
inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def getvalues(mystr):
    mylen = len(mystr)
    firstnum = ''
    lastnum = ''
    #findfirst
    for i in range(mylen):
        if debug:
            print(i,mystr[i])
        if mystr[i].isdigit():
            firstnum = mystr[i]
            break
    for j in range((mylen - 1),-1,-1):
        if debug:
            print(j, mystr[j])
        if mystr[j].isdigit():
            lastnum = mystr[j]
            break
    myvalue = firstnum+lastnum
    print(myvalue)
    return(myvalue)

def main():
    load_data()
    total_value = 0
    for item in inputData:
        strnum = getvalues(item)
        print(int(strnum))
        total_value = total_value + int(strnum)
    print('total ',total_value)

if __name__ == "__main__":
    main()