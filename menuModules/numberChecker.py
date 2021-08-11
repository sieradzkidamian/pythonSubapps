def checkNumbers():
    numbers = []
    userNumber = 'x'
    sumOfNumbers = {
        'lessThan': 0,
        'biggerThan': 0,
        'equalTo': 0
    }

    print('Wpisz liczby do porówniania, jeśli chcesz zakończyć wpisywanie użyj klawisza enter')
    while(userNumber != ''):
        userNumber = input('Podaj liczbę: ')
        checkIfInt = userNumber.isnumeric()
        if(checkIfInt):
            numbers.append(userNumber)
            print(numbers)
        elif(userNumber == ''):
            break
        elif(not checkIfInt):
            print('To nie jest liczba!')
            




    for x in numbers:
        if str(x) < '10':
            sumOfNumbers['lessThan'] = sumOfNumbers.get('lessThan', 0) +1
        elif str(x) > '10':
            sumOfNumbers['biggerThan'] = sumOfNumbers.get('biggerThan', 0) +1
        else:
            sumOfNumbers['equalTo'] = sumOfNumbers.get('equalTo', 0) +1 
                
    print('Liczb mniejszych od 10 jest: ' + str(sumOfNumbers['lessThan']))
    print('Liczb większych od 10 jest: ' + str(sumOfNumbers['biggerThan']))
    print('Liczb równych zero jest: ' + str(sumOfNumbers['equalTo']))