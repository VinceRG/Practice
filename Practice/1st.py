given_nums = [3, 1 , 7 , 9]
target = 10

def two_sums(given_nums , target):
    for i in range(len(given_nums)):
        for j in range(i + 1, len(given_nums)):
            if given_nums [i] + given_nums [j] == target:
                print({i},{j})
                return [i,j]
            else:
                print ("No Solution")

two_sums(given_nums, target)