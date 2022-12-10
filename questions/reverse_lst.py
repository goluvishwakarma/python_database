# lst = [1, 2, 3, 4, 5]
lst = list(map(int, input("Enter array elements: ").split(" ")))

for i in range((-len(lst) + (len(lst) - 1)), -(len(lst) + 1), -1):  # -1, -5, -1
    print(lst[i], end=" ")

# start = 0
# stop = len(lst) - 1
# while start < stop:
#     lst[start], lst[stop] = lst[stop], lst[start]
#     start += 1
#     stop -= 1
# print(lst)
