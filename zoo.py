from itertools import permutations

class Animal():
    def __init__(self, specie, gender):
        self.specie = specie
        self.gender = gender


def solution(k, males, females):
    if len(males) != len(females):
        raise Exception("Bad input")

    animals = []

    for i in range(len(males)):
        for j in range(males[i]) :
            animals.append(Animal(i, 0))

    for i in range(len(females)):
        for j in range(females[i]):
            animals.append(Animal(i, 1))

    all_perm = permutations(animals)

    max_groups = 0
    for perm in all_perm:
        count = 0
        
        for i in range(len(perm) // k):
            sub_list = perm[i*k : (i*k + k)]
            correct_gender_group = True
            correct_specie_group = True

            for j in range(len(sub_list) - 1):
                if sub_list[j].gender != sub_list[j+1].gender:
                    correct_gender_group = False
                    break

            for j in range(len(sub_list) - 1):
                if sub_list[j].specie != sub_list[j+1].specie:
                    correct_gender_group = False
                    break

            if correct_gender_group or correct_specie_group: 
                count += 1

        max_groups = max(max_groups, count)

    return max_groups


males = [2, 1, 1]
females = [2, 2, 2]        

print(solution(4, males, females))            
    

    