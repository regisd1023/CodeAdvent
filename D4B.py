'''
How many pairs overlap at all
'''
#My_File = 'sample.txt'
My_File = 'D4Adata.txt'


inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def make_set(mystring):
    # expecting "5-7" and returns a set {5,6,7}
    set_bounds = mystring.split('-')
    lower = int(set_bounds[0])
    upper = int(set_bounds[1]) + 1
    myset = set(range(lower,upper))
    return(myset)

def do_i_overlap(myline):
    # expecting myline to look like "5-7,7-9"
    sections = myline.split(',')
    set1 = make_set(sections[0])
    set2 = make_set(sections[1])
    if (len(set1.intersection(set2))):
        return(True)
    else:
        return(False)

def main():
    load_data()
    num_pairs = 0
    for line in inputData:
        if do_i_overlap(line):
            num_pairs = num_pairs + 1

    print(num_pairs)



if __name__ == "__main__":
    main()