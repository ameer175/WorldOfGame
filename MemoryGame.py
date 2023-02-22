import os
import random
import time
from Utils import Screen_cleaner
def generate_sequence(Difficulty):
    ListRandomNumber = []
    for i in range(Difficulty):
        ListRandomNumber.append(random.randint(1,101))
    print("the List is: ", ListRandomNumber)
    time.sleep(0.7)
    Screen_cleaner()
    return ListRandomNumber

def get_list_from_user(Difficulty):
    ListUserNumber = []
    for i in range(Difficulty):
        try:
            num = int(input("Get me a" + " " + str(Difficulty - i) + " " + "value: "))
            ListUserNumber.append(num)
        except Exception as e:
            print("--------------------------------------------------\n","the Type Error is: ",type(e) , "try again\n","-----------------------------------------------------")
            get_list_from_user(Difficulty)

    return ListUserNumber

def is_list_equal(Difficulty):
    ListA = generate_sequence(Difficulty)
    ListB = get_list_from_user(Difficulty)
    return (ListA == ListB)

def play(Difficulty):
    return is_list_equal(Difficulty)