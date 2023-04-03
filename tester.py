from test_cases_generator import generator1, generator2
from zoo import solution1, solution2
from colorama import Fore

algorithm = {"1" : solution1, "2" : solution2}

print("Solutions:")
print("1: First Aproximation", "2: Second Aproximation", "3: Greedy")
algo1 = input("Choose the first algorithm \n")
algo2 = input("Choose the second algorithm \n")

if algo1 == "1" or algo2 == "1":
    test_cases_number = int(input("How many test cases you want to generate? \n"))
    test_cases = generator1(test_cases_number)

else:
    test_cases_number = int(input("How many test cases you want to generate? \n"))
    test_cases = generator2(test_cases_number)

for case in test_cases:
    answer1 = algorithm[algo1](case[0], case[1], case[2])
    answer2 = algorithm[algo2](case[0], case[1], case[2])
    match = answer1 == answer2

    if match:
        print(Fore.GREEN, f"k: {case[0]}, males: {case[1]}, females: {case[2]}, answer1:{answer1}, answer2:{answer2}, good")

    else:
        print(Fore.GREEN, f"k: {case[0]}, males: {case[1]}, females: {case[2]}, answer1:{answer1}, answer2:{answer2}, bad")

print(Fore.RESET, "")



