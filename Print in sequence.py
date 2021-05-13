arr = []

n = int(input())

for i in range(n):
    arr.append(int(input()))

# print(arr)
count_1 = 0;
count_0 = 0;
count_2 = 0;

for i in range(n):
    if (arr[i] == 1):
        count_1 += 1;

    if (arr[i] == 0):
        count_0 += 1;

    if (arr[i] == 2):
        count_2 += 1;

for i in range(count_1):
    print("1 ", end="");

for i in range(count_0):
    print("0 ", end="");

for i in range(count_2):
    print("2 ", end="");

"""
Given a list A of integer numbers that have values coming from SET=(0, 1, 2). The task is to put then the output should be 1 1 0 0 2 2
all ones first, then all Os, then 2s at last.

For example, List A[] = {0, 2, 1, 0, 1, 2}
Output : 1 1 0 0 2 2
"""