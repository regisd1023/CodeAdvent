# template for advent 2023

#debug=True
debug=False
#My_File = '2024-myfile1.txt'
My_File = '24day2a.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def all_increase(mylist):
    result = False
    if debug:
        print('is_inc ',mylist)
    for x in range(len(mylist)):
        if x == 0:
            continue
        else:
            if mylist[x-1] < mylist[x]:
                result = True
            else:
                return(False)
    return(result)

def all_decrease(mylist):
    result = False
    if debug:
        print('is_dec ',mylist)
    for x in range(len(mylist)):
        if x == 0:
            continue
        else:
            if mylist[x-1] > mylist[x]:
                result = True
            else:
                return(False)
    return(result)

def diffs_okay(mylist):
    for x in range(len(mylist)):
        if x == 0:
            continue
        else:
            mydiff = abs(mylist[x] - mylist[x-1])
            if ((mydiff > 0) and (mydiff < 4)):
                if debug:
                    print('diff okay',mydiff)
                result = True
            else:
                return(False)
    if debug:
        print("result ",result)
    return(result)



def is_line_safe(mylist):
    result = False
    allone = False
    if all_decrease(mylist):
        allone = True
        if debug:
            print('all decrease ',mylist)
    elif all_increase(mylist):
        allone = True
        if debug:
            print('all decrease ',mylist)
    else:
        if debug:
            print('line out of order', mylist)
        return(False)

    if diffs_okay(mylist):
        if allone:
            return(True)
        else:
            return(False)

def problem_dampen(mylist):
    for x in range(len(mylist)):
        tmplist = mylist.copy()
        del tmplist[x]
        if is_line_safe(tmplist):
            if debug:
                print(mylist,' dampened at index ',x)
            return(True)
    return(False)


def main():
    safecount = 0
    load_data()
    for myline in inputData:
        thisline = []
        words = myline.split()
        for word in range(len(words)):
            thisline.append(int(words[word]))
        if debug:
            print('thisline ',thisline)
        if is_line_safe(thisline):
            safecount = safecount + 1
            if debug:
                print("line good", thisline)
        else:
            if debug:
                print('line bad',thisline)
            if problem_dampen(thisline):
                if debug:
                    print('but dampened')
                safecount = safecount + 1
    print('count is ', safecount)

if __name__ == "__main__":
    main()
