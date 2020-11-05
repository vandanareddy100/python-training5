
def even(num):
    return(num)
list1 = [10,23,2,25,36,47,45,8,79,56,31]
    # lambda exp.
even = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ", even)
print(even)
