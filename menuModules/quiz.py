import random

def quiz():
    number = random.randint(0, 9)
    userNumber = input("Zgadnij liczbę: ")
    attempts = 0

    while (userNumber != "exit"):
        if int(userNumber) < int(number):
            print("Twoja liczba jest mniejsza niż wylosowana")
            attempts += 1
            userNumber = input("Zgadnij liczbę: ")
        elif int(userNumber) > int(number):
            print("Twoja liczba jest większa niż wylosowana")
            attempts += 1
            userNumber = input("Zgadnij liczbę: ")
        else:
            print("Brawo! Udało Ci się odgadnąć liczbę")
            attempts += 1
            print("Ilość prób: " + str(attempts))
            break



