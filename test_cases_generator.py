import random 

def generator1(test_cases_number):
    cases = []

    for i in range(test_cases_number):
        n = random.randint(2, 4)
        males = []
        females = []
        animals_available = 8
        k = random.randint(1, 8)

        for i in range(n):
            if animals_available <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, animals_available)

            males.append(r1)
            animals_available -= r1

        for i in range(n):
            if animals_available <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, animals_available)

            females.append(r1)
            animals_available -= r1

        cases.append((k, males, females))

    return cases


def generator2(test_cases_number):
    test_cases = []

    for i in range(test_cases_number):
        n = random.randint(1, 7)
        males = []
        females = []
        total = 0

        for i in range(n):
            mi = 0    
            fi = 0

            while mi + fi == 0:
                mi = random.randint(0, 20)
                fi = random.randint(0, 20)
            
            total += mi + fi
            males.append(mi)
            females.append(fi)

        k = random.randint(1, 10)
        
        test_cases.append((k, males, females))

    return test_cases
    

def generator3(test_cases_number):
    test_cases = []

    for i in range(test_cases_number):
        n = random.randint(1, 50)
        males = []
        females = []
        total = 0

        for i in range(n):
            mi = 0    
            fi = 0

            while mi + fi == 0:
                mi = random.randint(0, 100)
                fi = random.randint(0, 100)
            
            total += mi + fi
            males.append(mi)
            females.append(fi)

        k = random.randint(1, total)
        
        test_cases.append((k, males, females))

    return test_cases