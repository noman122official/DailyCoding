def rpt_element(lst):
    count = {}

    for i in range(len(lst)):
        if lst[i] in count.keys():
            count[lst[i]] = count[lst[i]] + 1
        else:
            count[lst[i]] = 1


    for i in range(len(lst)):
        if count[lst[i]] > 1:
            return (lst[i], i)

    return -1
lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
	ele = int(input("Enter elements: "))
	lst.append(ele)
print(rpt_element(lst))
