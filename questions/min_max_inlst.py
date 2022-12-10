# date: 20.11.21, @author...


"""
l=list(map(int,input("Enter array elements:").split(" ")))

min1=l[0]
for i in range(1,len(l)):
    if(l[i]<min1):
        min1=l[i]
print(min1)
"""


def min_element(lst):
    low = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < low:
            low = lst[i]

    return low


def max_element(lst):
    high = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > high:
            high = lst[i]

    return high


lst = [7, 4, 1, 0, 5, 2, 9, 3, 8, -1]
print(("Min Sum: ", min_element(lst)))  # output: -1
print(("Max Sum: ", max_element(lst)))  # output: 9
