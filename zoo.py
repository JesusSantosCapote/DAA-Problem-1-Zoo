from itertools import permutations, combinations

class Animal():
    def __init__(self, specie, gender):
        self.specie = specie
        self.gender = gender

    def __str__(self):
        return f"({self.gender}, {self.specie})" 


def solution1(k, males, females):
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
                    correct_specie_group = False
                    break

            if correct_gender_group or correct_specie_group: 
                count += 1
                # for a in sub_list:
                #     print(a)
                # print('\n')

        max_groups = max(max_groups, count)

    return max_groups


def solution2(k, males, females):
    valid_cols = []
    males_number = 0
    females_number = 0
    total_groups = 0

    def backtrack(cols, index, males_n, females_n, cols_groups_formed):
        nonlocal total_groups

        if index == len(cols):
            groups = males_n // k + females_n // k + cols_groups_formed
            total_groups = max(total_groups, groups)
            
        else:        
            for j in range(k + 1):
                if j <= males[cols[index]]  and k - j <= females[cols[index]]:
                    backtrack(cols, index + 1, males_n - j, females_n - k + j, cols_groups_formed + 1)
            

    for i in range(len(males)):
        if males[i] + females[i] >= k:
            valid_cols.append(i)

        males_number += males[i]
        females_number += females[i]

    if len(valid_cols) == 0: 
        return males_number // k + females_number // k

    cols_comb = []

    for i in range(len(males) + 1):
        comb = combinations(valid_cols, i)
        cols_comb.extend(comb)

    for cols_group in cols_comb:
        temp_males_number = males_number
        temp_females_number = females_number

        backtrack(cols_group, 0, temp_males_number, temp_females_number, 0)

    return total_groups


# males = [0, 0, 0]
# females = [0, 4, 0]

# males1 = [1, 1, 1]
# females1 = [4, 3, 0]

# males2 = [0, 0, 0]  
# females2 = [4, 3, 1]

# males3 = [0, 0, 0]
# females3 = [3, 3, 4]

# males4 = [1, 1, 4]
# females4 = [1, 1, 2]

# males5 = [1, 1, 1]
# females5 = [4, 3, 0]

# males6 = [5, 0, 0]
# females6 = [4, 1, 0]

# males7 = [1, 1, 1]
# females7 = [3, 3, 1]

# k = 2

# print(solution1(k, males2, females2))

# print(solution1(k, males1, females1) == solution2(k, males1, females1))

# print(solution1(k, males2, females2) == solution2(k, males2, females2))

# print(solution1(k, males3, females3) == solution2(k, males3, females3))

# print(solution1(k, males4, females4) == solution2(k, males4, females4))

# print(solution1(k, males5, females5) == solution2(k, males5, females5))

# print(solution1(k, males6, females6) == solution2(k, males6, females6))

# print(solution1(k, males7, females7) == solution2(k, males7, females7))

    