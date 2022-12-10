
def searchIndex():

    lst = list(map(int, input("Enter array elements: ").split(" ")))
    e = int(input("Enter the element to find: "))

    for i in range(len(lst)):
        if lst[i] == e:
            print("element at index: ", i)
            break

    else:
        print("Element not found !")


searchIndex()
