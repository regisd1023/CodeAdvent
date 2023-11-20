'''
happy little trees

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
'''
#My_File = 'sample.txt'
My_File = 'D8A.txt'

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
    visible_up = True
    visible_down = True
    visible_left = True
    visible_right = True
    x = pointlist[0]
    y = pointlist[1]
    my_height = treearray[x][y]
    for i in range(0,x):
        if my_height <= treearray[i][y]:
            visible_left = False
    for i in range((x + 1),columns):
        if my_height <= treearray[i][y]:
            visible_right = False
    for j in range(0,y):
        if my_height <= treearray[x][j]:
            visible_up = False
    for j in range((y + 1),rows):
        if my_height <= treearray[x][j]:
            visible_down = False
    am_i_visible = visible_up or visible_down or visible_left or visible_right
    return(am_i_visible)


def main():
    global rows,columns
    load_data()
    rows = len(inputData)
    columns = len(inputData[0])
    # load treearray
    for y in range(columns):
        mylist = list(inputData[y])
        treearray.append(mylist)

#top and bottom
    y = 0
    for x in range(columns):
        visible_trees.add(tuple([x,y]))
    y = columns - 1
    for x in range(columns):
        visible_trees.add(tuple([x,y]))
#left and right sides
    x = 0
    for y in range(rows):
        visible_trees.add(tuple([x,y]))
    x = rows - 1
    for y in range(rows):
        visible_trees.add(tuple([x,y]))
    print('edges',len(visible_trees))
#okay, now we do the inside parts

    for x in range(1,(columns - 1)):
        for y in range(1,(rows - 1)):
            if examine_tree([x,y]):
                visible_trees.add(tuple([x,y]))



    print(len(visible_trees))
    print(visible_trees)



if __name__ == "__main__":
    main()



