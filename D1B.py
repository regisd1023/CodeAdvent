'''
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''
#My_File = 'sample.txt'
My_File = 'D1A-input.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()


def main():
    load_data()
    elf = {}
    elfcount = 1
    calcount = 0
    elf[1] = 0
    for line in inputData:
        if len(line) > 0:
            calnum = int(line)
            elf[elfcount] = elf[elfcount] + calnum
        else:
            elfcount = elfcount + 1
            elf[elfcount] = 0
    elflist = []
    totalcal = 0
    topcount = 0
    for k in sorted(elf,key=elf.get,reverse=True):
        topcount = topcount + 1
        if topcount > 3:
            break
        else:
            totalcal = totalcal + elf[k]
        #print(k,elf[k])
        #elflist.append[[k,elf[k]]]
    print(totalcal)
    #elf_max = max(elf,key=elf.get)
    #print("elf:",elf_max,"\t value:",elf[elf_max])
    #print(elf)



if __name__ == "__main__":
    main()