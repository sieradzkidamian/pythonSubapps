from menuModules.quiz import quiz
from menuModules.numberChecker import checkNumbers
from menuModules.randomNumber import randomNumberList
from menuModules.vehicle import vehicleAdd

def isContinue():
    print('Czy chcesz kontynuować? ')
    userDecision = input("Kliknij enter aby kontynuować lub wstaw dowolny znak aby anulować.")
    if(not userDecision):
        return False
    else:
        return True

userDecision = ''
while(userDecision != '5'):
    print('Wybierz pozycje z menu: ')
    print('1. Zgadywanka.')
    print('2. Porównywarka liczb do 10. ')
    print('3. Generuj losowe liczby i zapisz do pliku. ')
    print('4. Dodaj swój pojazd do bazy danych. ')
    print('5. Wyjście')
    userDecision = input('Podaj numer pozycji z menu: ')
    if(userDecision == '1'):
        quiz()
        try: 
            while isContinue():
                userDecision = '5'
                print('Zapraszamy ponownie! :)')
                break
        except:
            print('Dziękujemy za gre! ')
    elif(userDecision == '2'):
        checkNumbers()
        try: 
            while isContinue():
                userDecision = '5'
                print('Zapraszamy ponownie! :)')
                break
        except:
            print('Dziękujemy za gre! ')
    elif(userDecision == '3'):
        randomNumberList()
        try: 
            while isContinue():
                userDecision = '5'
                print('Zapraszamy ponownie! :)')
                break
        except:
            print('Widzimy się następnym razem! ')
    elif(userDecision == '4'):
        vehicleAdd()
        try: 
            while isContinue():
                userDecision = '5'
                print('Dziękujemy że z nami byłeś! :)')
                break
        except:
            print('Dziękujemy za gre! ')
    else:
        print('Do następnego razu! ;) ')
        break


