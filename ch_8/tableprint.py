tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printtable(td):
    colswidth = [len(max(i, key=len)) for i in td]
    print(colswidth)

    for i in range(len(td[0])):
        print(td[0][i].rjust(colswidth[0]),end=" ")
        print(td[1][i].rjust(colswidth[1]),end=" ")
        print(td[2][i].rjust(colswidth[2]),end=" ")
        print()

printtable(tableData)
