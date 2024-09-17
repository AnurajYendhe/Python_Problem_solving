def CheckPrime(No):
    PrimeNum = list()
    counter = 0
    for i in range(2,No,1):
        if(No % i ) == 0:
            counter = counter + 1

    if(counter == 0):
        PrimeNum.append(No)

    return PrimeNum