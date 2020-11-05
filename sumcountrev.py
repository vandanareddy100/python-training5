def sum_count_reverse(num):
    return num
def sum(x,y):
    return x+y
result=sum(10,20)
print("The sum is",result)
print("The sum is",sum(100,200))
def count(num):
    list=[18,27,8,15,18,24,18,15,8]
    print("the count is:" ,list.count(num))
count(18)
def reverse(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = (rev*10)+rem
        num = num//10
    print("%d" %rev )
reverse(1457)
