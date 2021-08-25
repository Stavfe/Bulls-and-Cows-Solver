# code written by Stavfe
# 25/08/2021
# https://github.com/Stavfe

import random

NUM_OF_DIGITS = 4


def compare_2_nums(a, b):
    """
    compare 2 numbers and tells how many bulls and cows in it
    :param a: str of first number
    :param b: str of second number
    :return: tuple (bulls,cows)
    """
    bulls = 0
    cows = 0
    for dig1 in range(NUM_OF_DIGITS):
        if a[dig1] == b[dig1]:
            bulls += 1
        for dig2 in range(NUM_OF_DIGITS):
            if a[dig1] == b[dig2]:
                cows += 1
    cows -= bulls  # becasue it includes the bulls
    return bulls, cows


def num_is_legit(num):
    """
    check if number is safe to use: no zeros, or duplicates, and in right size
    :param num: str number
    :return: true if allowed number
    """
    if len(num) != NUM_OF_DIGITS:
        return False
    for i in range(len(num)):
        if num[i] == '0':
            return False
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                return False

    return True


def bulls_cows_algo():
    """
    main algorithm, runs the interactive programm
    :return: none
    """
    print("\nWelcome to the game Bulls&Cows, guess a number and let the programm"
          "find your guess.\n\n"
          "Think of a number of 4 digits, no duplicates, and no zeros.\n"
          "answer the questions by assigning 2 numbers each time "
          "like that-\n\"Bulls\" \"Cows\"\n"
          "Example: the number is 1234, the guess was 2134, "
          "so your answer should be \'2 2\'\n"
          "Good luck!\n"
          )
    # create a list of all allowed numbers
    possible_nums_list = [str(num) for num in
                          range(10 ** (NUM_OF_DIGITS - 1), 10 ** NUM_OF_DIGITS)
                          if num_is_legit(str(num))]
    counter = 0  # what iteration of the game we are in
    number_try = None
    # run game as long theres more than one option
    while len(possible_nums_list) > 1:
        counter += 1
        # get random number to ask for
        number_try = possible_nums_list[
            random.randint(0, len(possible_nums_list))]
        print("Question #", str(counter), ": ", str(number_try))
        answer_bulls, answer_cows = input("how many cows and bulls?\n").split()
        # instead of cleaning old list, faster to create new one and replace
        new_list = []

        for num in possible_nums_list:
            # check if numbers in list fits current result, if not, remove them
            if compare_2_nums(num, str(number_try)) == (
                    int(answer_bulls), int(answer_cows)):
                new_list.append(num)
        possible_nums_list = new_list
    if( ~len(possible_nums_list)):
        print("you made a mistake along the way, there's no such number")
        return
    print("your guess is", possible_nums_list[0])
    return


if __name__ == '__main__':
    bulls_cows_algo()
