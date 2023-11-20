'''
happy little trees

30373
25512
65332
33549
35390


A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
correct sample value is [2.3]
'''
My_File = 'sample.txt'
#My_File = 'D8A.txt'

visible_trees = set()

treecount = 0

treearray = []
inputData = []
def load_data():
    fhand = open(My_File)
    for line in fhand:
        inputData.append(line.strip())
    fhand.close()
    return()

def examine_tree(pointlist):
    global rows, columns
    visible_up = 1
    visible_down = 1
    visible_left = 1
    visible_right = 1
    x = pointlist[0]
    y = pointlist[1]
    my_height = treearray[x][y]
    print('looking at tree[',x,',',y,']',' = ',treearray[x][y])
    numtrees = 1
    for i in range(1,x):
        print('i', i)
        if my_height <= treearray[i][y]:
            visible_left = numtrees
            break
        else:
            numtrees = numtrees + 1
    numtrees = 1
    for i in range((x + 1),columns - 1):
        if my_height <= treearray[i][y]:
            visible_right =  numtrees
            break
        else:
            numtrees = numtrees+ 1
    numtrees = 1
    for j in range(1,y):
        if my_height <= treearray[x][j]:
            visible_up = numtrees
            break
        else:
            numtrees = numtrees + 1
    numtrees = 1
    for j in range((y + 1),rows - 1):
        if my_height <= treearray[x][j]:
            visible_down = numtrees
            break
        else:
            numtrees = numtrees + 1
    visible_score = visible_up * visible_down * visible_left * visible_right
    print(visible_up, visible_down, visible_left, visible_right)
    print(visible_score)
    return(visible_score)


def main():
    global rows,columns
    load_data()
    rows = len(inputData)
    columns = len(inputData[0])
    # load treearray
    for y in range(columns):
        mylist = list(inputData[y])
        treearray.append(mylist)

    max_view = 0
    for x in range(1,(columns - 1)):
        for y in range(1,(rows - 1)):
            thistree = examine_tree([x,y])
            print('treearray[',x,'][',y,'] = ',thistree)
            if (thistree > max_view):
                print('max_view now',thistree)
                max_view = thistree
    print('max',max_view)


if __name__ == "__main__":
    main()



