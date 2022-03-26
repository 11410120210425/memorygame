'''one line memory game
There are 20 digits each 10 digits in sequence from 0 to 9,
There are 20 letters, each letter repeated twice,
The letters are arranged in random order,
It consists of two players. Each player chooses two numbers.
 If the two numbers contain the same letter, the two numbers are replaced with '*',  the score of this player is increased by 1 and two numbers arenot chosen again.
 else the two numbers contain two different letters, it is printed list of numbers and the score = 0
 '''
import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J']  # Repeat each character twice
list1 = random.sample(list1, 20)  # Random order of character
list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         "0"]  # Each player chooses two numbers
print(list1)
# scores initial assumption
score1 = 0
score2 = 0
for i in range(5):
    print(list2)
    print("the first player,enter two numbers ")
    num1, num2 = int(input()), int(input())  # player enter 2 num
    last1 = list2[num1 - 1]
    last2 = list2[num2 - 1]
    list2[num1 - 1] = list1[num1 - 1]
    list2[num2 - 1] = list1[num2 - 1]
    print(list2)
    # check num1=num2
    if list1[num1 - 1] == list1[num2 - 1]:
        score1 += 1
        list2[num1 - 1], list2[num2 - 1] = "*", "*"  # When the two numbers are equal, they are replaced with'*'
    else:
        list2[num1 - 1] = last1
        list2[num2 - 1] = last2

    print(list2)  # When the two numbers are not equal,  printed list of num
    print("score1:")
    print(score1)

    print("the second player,enter two numbers ")
    num1, num2 = int(input()), int(input())  # player enter 2 num
    last1 = list2[num1 - 1]
    last2 = list2[num2 - 1]
    list2[num1 - 1] = list1[num1 - 1]
    list2[num2 - 1] = list1[num2 - 1]
    print(list2)
    # check num1=num2
    if list1[num1 - 1] == list1[num2 - 1]:
        score2 += 1
        list2[num1 - 1], list2[num2 - 1] = "*", "*"  # When the two numbers are equal, they are replaced with'*'
    else:
        list2[num1 - 1] = last1
        list2[num2 - 1] = last2
    print(list2)
    print("score2:")  # When the two numbers are not equal,  printed list of num
    print(score2)

if score1 > score2:  # Check out the biggest score
    print("the player 1 is won ")
elif (score1 < score2):
    print("the player 2 is won")
else:
    print()
