# template for advent 2023

debug=True
debug=False

#My_File = '2024-myfile1.txt'
My_File = '2024day1a.txt'
inputData = []
list1 = []
list2 = []

def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def get_distance(x,y):
    return(abs(x-y))

def getscore(leftnum):
    seen = 0
    for rightnum in list2:
        if rightnum == leftnum:
            seen = seen + 1
            if debug:
                print(leftnum," seen ",rightnum)
        else:
            continue
    similarity = leftnum * seen
    if debug:
        print("similarity score ",similarity)
    return(similarity)

def main():
    similarity_total = 0
    total_dist = 0
    load_data()
    for line in inputData:
        if len(line) < 4:
            exit(0)
        words = line.split()
        list1.append(int(words[0]))
        list1.sort()
        list2.append(int(words[1]))
        list2.sort()
    if debug:
        print(inputData)
        print(list1)
        print(list2)
        print("length: ",len(list1))
    for count in range(len(list1)):
        similarity_total = similarity_total + getscore(list1[count])
    print("TOTAL", similarity_total)


if __name__ == "__main__":
    main()
