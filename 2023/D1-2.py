
debug = True

#debug = False

#My_File = 'D1input.txt'
My_File = 'D1-2-sample.txt'
inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def sanitize_item(mystr):
    mystr = mystr.replace('one','1')
    mystr = mystr.replace('two','2')
    mystr = mystr.replace('three','3')
    mystr = mystr.replace('four','4')
    mystr = mystr.replace('five','5')
    mystr = mystr.replace('six','6')
    mystr = mystr.replace('seven','7')
    mystr = mystr.replace('eight','8')
    mystr = mystr.replace('nine','9')
    return(mystr)

def getvalues(mystr):
    mylen = len(mystr)
    firstnum = ''
    lastnum = ''

    num_i = 0
    num_j = 0

    for i in range(mylen):
        if debug:
            print(i,mystr[i])
        if mystr[i].isdigit():
            firstnum = mystr[i]
            num_i = i
            break
    for j in range((mylen - 1),-1,-1):
        if debug:
            print(j, mystr[j])
        if mystr[j].isdigit():
            lastnum = mystr[j]
            num_j = j
            break
    myvalue = firstnum+lastnum
    print(num_i,num_j)
    print('value',myvalue)
    return(myvalue)

def main():
    load_data()
    total_value = 0
    for item2 in inputData:
        item = sanitize_item(item2)
        if True:
            print('was',item2,'now processing ', item)
        strnum = ''
        strnum = getvalues(item)
        print(strnum)
        total_value = total_value + int(strnum)
    print('total ',total_value)

if __name__ == "__main__":
    main()


