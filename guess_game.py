# import random as rd
# from typing import Counter 

# figure = input("input figures here : ")
# figure = figure.split(" ")

# fig = map(lambda a: int(a), figure)
# fid = list(fig)

# rand = rd.randrange(fid[0], fid[1])
# print(rand)

# tries = 0 # add a counter and make it empty at first

# while True:

#     guess_number = input("Guess number ")
#     guess_number = int(guess_number)
#     tries += 1 # increment at every try

#     if guess_number == rand:

#         print("YOU WIN")
#         break

#     elif guess_number < rand:

#         print("HINT: YOUR NUMBER IS LESS")

#     elif guess_number > rand:

#         print("HINT: YOUR NUMBER IS MORE")

#     else:

#         pass

# print("You tried :", tries, "times") # print tries


# import random as rd

# def collect_data():

#     figure = input("input figures  \n> ")
#     name   = input("input name  \n> ")

#     figure = figure.split(" ")

#     fig = map(lambda a: int(a), figure)
#     fid = list(fig)

#     rand = rd.randrange(fid[0], fid[1])
#     print(rand)
#     return rand, name

# def play():

#     tries = 0 # add a counter and make it empty at first

#     rand, name = collect_data()

#     while True:

#         guess_number = input("Guess number ")
#         guess_number = int(guess_number) # TYPE CASTING
#         tries += 1 # increment at every try

#         if guess_number == rand:

#             print("YOU WIN")
#             break

#         elif guess_number < rand:

#             print("HINT: YOUR NUMBER IS LESS")

#         elif guess_number > rand:

#             print("HINT: YOUR NUMBER IS MORE")

#         else:

#             pass

#     write_to_file(name, tries)
#     print("You tried :", tries, "times") # print tries


# # with open("database.csv", "a") as our_log_file:

# #     name = "atha"
# #     tries = 6
# #     our_log_file.write(f"{name},{tries}")

# def write_to_file(name, tries):

#     with open("database.csv", "a") as our_log_file: # FILE OPEN CONTEXT MANAGER

#         our_log_file.write(f"{name},{tries}\n")

#     print("Logged session.!!")


# play()

# SET PLAY LIMIT TO 10 TRIES MAX AND ALSO DELAY 10SECS THEN RESET
import random as rd
import time

def collect_data():

    figure = input("input figures  \n> ")
    name   = input("input name  \n> ")

    figure = figure.split(" ")

    fig = map(lambda a: int(a), figure)
    fid = list(fig)

    rand = rd.randrange(fid[0], fid[1])
    print(rand)
    return rand, name

def play():

    limit = 1
    tries = 0 # add a counter and make it empty at first

    rand, name = collect_data()

    while True:

        guess_number = input("Guess number ")
        guess_number = int(guess_number) # TYPE CASTING
        tries += 1 # increment at every try
        limit += 1

        if guess_number == rand:

            print("YOU WIN")
            break

        elif guess_number < rand:

            print("HINT: YOUR NUMBER IS LESS")

        elif guess_number > rand:

            print("HINT: YOUR NUMBER IS MORE")
        
        if limit == 10:
            print("You missed it ", tries, "times")
            print("We are now delaying you.")
            limit = 1
            time.sleep(10)

    write_to_file(name, tries)
    print("You tried :", tries, "times") # print tries


def write_to_file(name, tries):

    with open("database.csv", "a") as our_log_file: # FILE OPEN CONTEXT MANAGER

        our_log_file.write(f"{name},{tries}\n")

    print("Logged session.!!")


# play()
print("Hello my name is : ", __name__)

if __name__ == "__main__":
    print("HEY THERE I AM THE MAIN MAN")