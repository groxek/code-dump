def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def binary_recursive(sp, target, l,r):
    if l>r: return -1
    mid_index = (l+r)//2
    mid_value = sp[mid_index]

    if target == mid_value:
        return mid_index

    elif target < mid_value:
        return binary_recursive(sp, target,l,mid_index-1)
    else:
        return binary_recursive(sp, target,mid_index+1,r)

mylist = [1,2,3,4,5,6,7,8,9]
print(binary_recursive(mylist, 10, 0, len(mylist)-1))