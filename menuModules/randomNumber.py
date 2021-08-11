def randomNumberList():
    import random

    numberOfDigits = int(input('Podaj ilość losowych liczb do wygenerowania i zapisania do pliku:' ))
    randomNumbers = []


    for x in range(numberOfDigits):
        randomNumber = random.randint(0, 100)
        randomNumbers.append(randomNumber)
        data_file = open('random_numbers.txt', 'a+', encoding='utf-8')
        data_file.write(str(randomNumbers))
        data_file.write('\n')
        data_file = open('random_numbers.txt', 'r', encoding='utf-8')    
    data_file.close()
