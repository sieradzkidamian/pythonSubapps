def vehicleAdd():
    import json

    data = {}
    nameUserVehicle = input('Wpisz markę pojazdu: ')
    registerPlate = input('Wpisz numer rejestracyjny pojazdu: ')

    vehicle = {
        'Marka': nameUserVehicle,
        'Numer rejestracyjny': registerPlate
    }

    with open('vehicleData.txt', 'a') as vehicleData:
        vehicleData.write(json.dumps(vehicle))

    print('Pojazd marki ' + nameUserVehicle + ' o numerach rejestracyjnych ' + registerPlate + ' został pomyślnie dodany do bazy danych')


