import random 

def generator1():
    n = random.randint(1, 4)
    cases = []

    for i in range(1000):
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

        
