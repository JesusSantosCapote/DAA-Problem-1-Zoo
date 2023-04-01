from test_cases_generator import generator1
from zoo import solution1, solution2
from colorama import Fore

cases = generator1()

for case in cases:
    result = solution1(case[0], case[1], case[2]) == solution2(case[0], case[1], case[2])

    if result:
        print(Fore.GREEN, result)
    else:
        print(Fore.RED, result)
