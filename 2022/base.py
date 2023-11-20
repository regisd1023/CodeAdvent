'''
base to load data and run main.
'''
My_File = 'sample.txt'

inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()


def main():
    load_data()


if __name__ == "__main__":
    main()