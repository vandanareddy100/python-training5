def odd(num):
    return(num)
list1 = [10,23,2,25,36,47,45,8,79,56,31]
    # lambda exp.
odd= list(filter(lambda x: (x % 2 != 0), list1))
print("odd numbers in the list: ", odd)
print(odd)
