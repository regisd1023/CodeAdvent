# template for advent 2023

debug=True
#debug=False

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
