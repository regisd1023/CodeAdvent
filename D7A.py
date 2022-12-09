'''
we're implementing du, here, aren't we?
'''
My_File = 'sample.txt'
#My_File = 'D7A.txt'



inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()



def main():
    load_data()
    for line in inputData:
        if line.startswith('$'):  #command
            if line.startswith('$ ls'):  # doing a listing
                continue
            elif line.startswith('$ dir '): # we have learned about a directory
                continue
            elif line.startswith('$ cd'): # moving to a new directory
                continue
        elif line.startswith('dir'): #lists a directory
            continue
        else: #should only bee file listings with size, name here
            words = line.split()
            try:
                print('int size',int(words[0]))
            except:
                print('wat')
            print('text ',words[0],'named ',words[1])


if __name__ == "__main__":
    main()