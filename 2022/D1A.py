'''
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''
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
    elf_max = max(elf,key=elf.get)
    print("elf:",elf_max,"\t value:",elf[elf_max])
    #print(elf)



if __name__ == "__main__":
    main()