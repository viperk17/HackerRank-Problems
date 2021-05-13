n = int(input())

if (n < 0 or n > 1000000):
    print("Wrong Input")

elif (n == 0):
    print(9);

else:
    arr = []

    for i in range(10):
        arr.append(9 - i);

    ans = 0;
    power = 1;

    while (n > 0):
        r = n % 10;
        replaced = arr[r];
        ans = ans + replaced * power;
        power *= 10;
        n = n // 10;
    print(ans)

"""
A game development company wants to design a brain game application for kids. There are different types of tasks to be designed for the game. Among all the tasks, there is one task in which each digit of an exisiting number has to be replaced with another digit. Consider the following table:

Existing Numbers: 0 1 2 3 4 5 6 7 8 9

Replace By: 9 8 7 6 5 4 3 2 1 0



Input : An integer N

Output : An integer with replaced values



Constraints :

1) 0 <= N <=1000000

2) If N value is out of above range Print ("Wrong Input")



Sample Input 1 : 105671

Sample Output 1 : 894328

Sample Input 2 : 1000001

Sample Output 2 : Wrong Input
"""