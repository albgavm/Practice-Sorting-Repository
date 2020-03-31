
list = [3,5,8,6,7,2]

def bubblesort(listname):
    passingcounter = 1

    while passingcounter < (len(listname)):

        # iterates per value in list
        listcounter = 0
        for i in listname:

            if listcounter < (len(listname) - 1):

                if listname[listcounter] > listname[listcounter + 1]:
                    temp = listname[listcounter]
                    listname[listcounter] = listname[listcounter + 1]
                    listname[listcounter + 1] = temp

                    listcounter += 1

                else:
                    listcounter += 1
            else:
                pass
        else:
            passingcounter += 1

    else:
        return(listname)


def selectionsort(listname):
    for firstposition in range(0, len(listname)):

        for innerposition in range(firstposition + 1, len(listname)):

            # if it gets the minimum and switches
            if listname[firstposition] > listname[innerposition]:
                temp = listname[firstposition]
                listname[firstposition] = listname[innerposition]
                listname[innerposition] = temp


    return(listname)

#test
bubblesort(list)
selectionsort(list)



