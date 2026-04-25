import random

user = input("Rock, Paper or Scissors (0/1/2)\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rand_num = random.randint(0,2)

if user == "0":   # rock
    print(rock)
    print("Computer: ")

    if rand_num == 0:
        print(rock)
        print("Draw")
    elif rand_num == 1:
        print(paper)
        print("You lose!")
    else:
        print(scissors)
        print("You win!")


if user == "1":  # paper
    print(paper)
    print("Computer: ")

    if rand_num == 1:
        print(paper)
        print("Draw")
    elif rand_num == 2:
        print(scissors)
        print("You lose!")
    else:
        print(rock)
        print("You win!")


if user == "2":  # scissors
    print(scissors)
    print("Computer: ")

    if rand_num == 2:
        print(scissors)
        print("Draw")
    elif rand_num == 0:
        print(rock)
        print("You lose!")
    else:
        print(paper)
        print("You win!")