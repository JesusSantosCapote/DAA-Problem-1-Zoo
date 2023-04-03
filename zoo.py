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


def solution3(k, males: list, females):
    A = 0
    B = 0
    for i in males:
        A = A + i
    for i in females:
        B = B + i
    T = A + B
    Ra = A%k
    Rb = B%k
    if Ra + Rb<k:
        return T//k
    use_of_column_i_in_A = []
    for i in range(len((males))):
        if males[i] + females[i] >= k and females[i]>0 and males[i]>0:
            temp_list =[]
                
            for i in range(max(k-females[i],1),min(males[i]+1,k)):
                temp_list.append(i)
            # if (max(k-females[i],0)== min(males[i]+1,k-1))
            use_of_column_i_in_A.append(temp_list)
    
    if len(use_of_column_i_in_A) == 0:
        return T//k - 1 

    dp = [[0 for i in range(k-1)] for i in range(len(use_of_column_i_in_A))]
    for i in use_of_column_i_in_A[0]:
        dp[0][i-1] = 1

    for i in range (1,len(dp)):
        for j in use_of_column_i_in_A[i]:
            dp[i][j-1] = 1
            for w in range(len(dp[i-1])):
                if dp[i-1][w]:
                    dp[i][w] = 1
                    temp_rest = (w + 1 + j)%k
                    dp[i][temp_rest-1] = 1
    needed_ti_sum_module_k = range(((A%k)-(T%k)+k)%k,A%k+1)

    for i in needed_ti_sum_module_k:
        if dp[len(dp)-1][i-1]:
            return T//k
    return T//k - 1
    